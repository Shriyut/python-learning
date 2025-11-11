from apache_beam.transforms.trigger import AfterCount, Repeatedly
import apache_beam as beam
from apache_beam.transforms.window import FixedWindows
from apache_beam.transforms.trigger import AfterWatermark
from apache_beam.testing.test_pipeline import TestPipeline
from apache_beam.testing.test_stream import TestStream
from apache_beam.testing.util import assert_that, equal_to
from collections import Counter


def aggregate_counts_matcher(expected):
    def matcher(actual):
        actual_counter = Counter()
        for k, v in actual:
            actual_counter[k] += v
        expected_counter = Counter(dict(expected))
        assert actual_counter == expected_counter, (
            f"Mismatch:\nActual: {actual_counter}\nExpected: {expected_counter}")
    return matcher


def after_count_example():
    with TestPipeline() as p:
        test_stream = (
            TestStream()
            .advance_watermark_to(0)
            .add_elements(['a', 'b', 'a'])
            .advance_watermark_to(5)
            .add_elements(['b'])
            .advance_watermark_to(10)
            .advance_watermark_to_infinity()
        )

        result = (
            p
            | test_stream
            | beam.Map(lambda x: (x, 1))
            | beam.WindowInto(
                FixedWindows(10),
                trigger=Repeatedly(AfterCount(2)),  # fires every 2 elements repeatedly
                accumulation_mode=beam.transforms.trigger.AccumulationMode.DISCARDING)
            | beam.CombinePerKey(sum)
        )

        # Multiple panes fire; expect multiple partial counts summed per firing.
        # raise BeamAssertException(msg)
        # apache_beam.testing.util.BeamAssertException: Failed assert: [('a', 1), ('a', 1), ('b', 1), ('b', 1)] == [('a', 2), ('b', 2)], unexpected elements [('a', 2), ('b', 2)], missing elements [('a', 1), ('a', 1), ('b', 1), ('b', 1)] [while running 'assert_that/Match']
        #  this happens because
        # discarding accumulation mode emits only the new counts since last trigger firing
        # With the trigger Repeatedly(AfterCount(2)), the pipeline fires early outputs every 2 elements.
        # This produces multiple panes with partial counts instead of a single final combined count.

        # | Problem                              | Fix                                   |
        # | ------------------------------------ | ------------------------------------- |
        # | Multiple partial count panes emitted | Use custom matcher aggregating counts |
        # | Want final combined counts in panes  | UseAccumulatinginstead of discarding  |
        # | Prefer single output per window      | UseAfterWatermarktrigger              |
        # assert_that(result, equal_to([('a', 1), ('a', 1), ('b', 1), ('b', 1)]))

        # fix
        expected = [('a', 2), ('b', 2)]
        assert_that(result, aggregate_counts_matcher(expected))
if __name__ == "__main__":
    after_count_example()
