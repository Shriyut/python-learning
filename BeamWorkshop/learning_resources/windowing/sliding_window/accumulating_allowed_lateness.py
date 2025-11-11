import apache_beam as beam
from apache_beam.transforms.window import SlidingWindows
from apache_beam.transforms.trigger import AfterWatermark, AccumulationMode
from apache_beam.testing.test_pipeline import TestPipeline
from apache_beam.testing.test_stream import TestStream
from apache_beam.testing.util import assert_that
from collections import Counter
from apache_beam.utils.timestamp import Duration

def aggregate_key_counts(elements):
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

def streaming_wordcount_with_allowed_lateness():
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
            .advance_watermark_to(40)  # Advance past window ends plus allowed lateness
            .advance_watermark_to_infinity()
        )

        result = (
            p
            | "Create TestStream" >> test_stream
            | "Split Words" >> beam.FlatMap(lambda x: x.split())
            | "Sliding Window with Allowed Lateness" >> beam.WindowInto(
                SlidingWindows(size=10, period=5),
                allowed_lateness=Duration(seconds=10),  # Keep window open 10s past watermark
                # trigger=AfterWatermark(late=AfterWatermark.PastEndOfWindow()),
                trigger=AfterWatermark(),
                accumulation_mode=AccumulationMode.ACCUMULATING)
            | "Pair with One" >> beam.Map(lambda w: (w, 1))
            | "Sum per Key" >> beam.CombinePerKey(sum)
        )

        # Expected counts accounting for sliding window overlaps and allowed lateness
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

        assert_that(result, aggregate_key_counts(expected_output))

if __name__ == "__main__":
    streaming_wordcount_with_allowed_lateness()
