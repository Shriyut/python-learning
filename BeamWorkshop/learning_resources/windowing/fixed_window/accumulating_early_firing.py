import apache_beam as beam
from apache_beam.transforms.window import FixedWindows
from apache_beam.transforms.trigger import AfterProcessingTime, Repeatedly, AccumulationMode
from apache_beam.testing.test_pipeline import TestPipeline
from apache_beam.testing.test_stream import TestStream
from apache_beam.testing.util import assert_that, equal_to
import apache_beam.transforms.trigger as trigger

def streaming_wordcount_with_early_trigger():

    # NOT SUPPORTED WITH PRISM RUNNER, because of TRiggering use FLink/Dataflow to test this
    with TestPipeline() as p:
        test_stream = (
            TestStream()
            .advance_watermark_to(0)
            .add_elements(["beam", "streaming", "beam"])  # Timestamps ~0
            .advance_watermark_to(5)
            .add_elements(["streaming", "test"])         # Timestamps ~5
            .advance_watermark_to(20)                     # Pass end of first and second windows
            .advance_watermark_to_infinity()
        )

        # trigger_strategy = trigger.Repeatedly(trigger.AfterCount(2))  # no processing-time, only element count

        # Use fixed windows of 10 seconds with an early trigger that fires repeatedly every 2 seconds of processing time.
        # This means results will be emitted multiple times before the window closes.
        result = (
            p
            | test_stream
            | beam.FlatMap(lambda x: x.split())
            | beam.WindowInto(
                FixedWindows(10),
                trigger=Repeatedly(AfterProcessingTime(2)), # Early firing every 2 seconds processing time
                # trigger=Repeatedly(AfterCount(2))  # element-count based triggers
                # trigger=trigger_strategy
                accumulation_mode=AccumulationMode.ACCUMULATING  # Accumulate counts across firings
            )
            | beam.Map(lambda w: (w, 1))
            | beam.CombinePerKey(sum)
        )

        # Expected output: multiple panes per window as the early trigger fires repeatedly.
        # The asserts here represent the expected final combined counts after all triggers.
        # Intermediate panes emit partial sums (not visible here).
        assert_that(result, equal_to([
            ('beam', 2),
            ('streaming', 2),
            ('test', 1)
        ]))

if __name__ == '__main__':
    streaming_wordcount_with_early_trigger()
