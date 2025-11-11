import apache_beam as beam
from apache_beam.transforms.window import SlidingWindows
from apache_beam.transforms.trigger import AfterCount, Repeatedly, AccumulationMode, AfterWatermark
from apache_beam.testing.test_pipeline import TestPipeline
from apache_beam.testing.test_stream import TestStream
from apache_beam.testing.util import assert_that
from collections import Counter

def aggregate_key_counts(elements):
    # Custom matcher callable that sums counts per key from actual output
    def matcher(actual):
        actual_counter = Counter()
        for k, v in actual:
            actual_counter[k] += v
        expected_counter = Counter()
        for k, v in elements:
            expected_counter[k] += v
        assert actual_counter == expected_counter, (
            f"Mismatch:\nActual: {actual_counter}\nExpected: {expected_counter}")
    return matcher

def streaming_wordcount_with_sliding_window_count_trigger():
    with TestPipeline() as p:
        test_stream = (
            TestStream()
            .advance_watermark_to(0)
            .add_elements(["beam", "streaming", "beam"])
            .advance_watermark_to(5)
            .add_elements(["streaming", "test"])
            .advance_watermark_to(10)
            .add_elements(["extra", "elements", "for", "more", "windows"])
            .advance_watermark_to(15)
            .add_elements(["even", "more", "data"])
            .advance_watermark_to(40)  # advance watermark well past last sliding window end
            .advance_watermark_to_infinity()
        )

        result = (
            p
            | "Create TestStream" >> test_stream
            | "Split words" >> beam.FlatMap(lambda x: x.split())
            | "Apply Sliding Window" >> beam.WindowInto(
                SlidingWindows(size=10, period=5),
                # trigger=Repeatedly(AfterCount(2)),
                trigger=AfterWatermark(), # fire only once when watermark passes window end
                # allowed_lateness=duration.Duration(seconds=10),  # Keep windows open 10s past watermark
                accumulation_mode=AccumulationMode.ACCUMULATING)
            | "Pair with one" >> beam.Map(lambda w: (w, 1))
            | "Sum per Key" >> beam.CombinePerKey(sum)
        )

        expected_output = [
            ("beam", 4),
            ("streaming", 4),
            ("test", 2),
            ("extra", 1),
            ("elements", 1),
            ("for", 1),
            ("more", 2),
            ("windows", 1),
            ("even", 1),
            ("data", 1)
        ]

        # trigger=Repeatedly(AfterCount(2)), -> causes assertion error
        # AssertionError: Mismatch:
        # Actual: Counter({'beam': 4, 'streaming': 2, 'more': 2})
        # Expected: Counter({'beam': 4, 'streaming': 4, 'test': 2, 'more': 2, 'extra': 1, 'elements': 1, 'for': 1, 'windows': 1, 'even': 1, 'data': 1}) [while running 'assert_that/Match']
        # this is because trigger waits for count of 2 before firing

        # trigger=AfterWatermark() causes the count for some elements to increase ( double basically)
        # AssertionError: Mismatch:
        # Actual: Counter({'beam': 4, 'streaming': 4, 'more': 4, 'test': 2, 'extra': 2, 'elements': 2, 'for': 2, 'windows': 2, 'even': 2, 'data': 2})
        # Expected: Counter({'beam': 4, 'streaming': 4, 'test': 2, 'more': 2, 'extra': 1, 'elements': 1, 'for': 1, 'windows': 1, 'even': 1, 'data': 1}) [while running 'assert_that/Match']
        # this is because we're usign sliding windows with overlapping intervals
        # each event falls into multiple sliding windows ( usually 2 in this case)
        # since we're accumulating counts per window and each window outputs separately
        # counts from overlapping windows add up in the aggregated output
        # the custom matcher sums counts across all output windows/panes, so overlapping counts accumulate
        # if we dont use custom amtcher we get callable error with assert that
        # but using fixed windows is more suitable for this use-case
        assert_that(result, aggregate_key_counts(expected_output))

if __name__ == "__main__":
    streaming_wordcount_with_sliding_window_count_trigger()
