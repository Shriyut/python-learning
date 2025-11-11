import apache_beam as beam
from apache_beam.transforms.window import SlidingWindows
from apache_beam.transforms.trigger import AfterCount, Repeatedly, AfterWatermark
from apache_beam.testing.test_pipeline import TestPipeline
from apache_beam.testing.test_stream import TestStream
from apache_beam.testing.util import assert_that
from collections import Counter

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

def streaming_wordcount_sliding_discarding_mode():
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
            .advance_watermark_to(40)
            .advance_watermark_to_infinity()
        )

        result = (
            p
            | test_stream
            | beam.FlatMap(lambda x: x.split())
            | beam.WindowInto(
                SlidingWindows(size=10, period=5),
                trigger=Repeatedly(AfterCount(2)),
                accumulation_mode=beam.transforms.trigger.AccumulationMode.DISCARDING)
            | beam.Map(lambda w: (w, 1))
            | beam.CombinePerKey(sum)
        )

        # Because of discarding mode and repeated triggers, expect pane-wise increments without accumulation.
        # This will have multiple smaller counts per key, so expected must include all emitted panes.
        expected_output = [
            ("beam", 2), ("beam", 2),
            ("streaming", 2), ("streaming", 1), ("streaming", 1),
            ("test", 1), ("test", 1),
            ("extra", 1), ("elements", 1),
            ("for", 1), ("more", 1), ("more", 1),
            ("windows", 1), ("even", 1), ("data", 1)
        ]

        # AssertionError: Mismatch:
        # Actual: Counter({'beam': 4, 'streaming': 2, 'more': 2})
        # Expected: Counter({'beam': 4, 'streaming': 4, 'test': 2, 'more': 2, 'extra': 1, 'elements': 1, 'for': 1, 'windows': 1, 'even': 1, 'data': 1}) [while running 'assert_that/Match']

        assert_that(result, aggregate_key_counts(expected_output))

if __name__ == "__main__":
    streaming_wordcount_sliding_discarding_mode()
