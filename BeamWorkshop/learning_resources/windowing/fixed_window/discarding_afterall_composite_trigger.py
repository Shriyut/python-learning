from apache_beam.transforms.trigger import AccumulationMode
from apache_beam.transforms.window import FixedWindows
from apache_beam.transforms.trigger import AfterWatermark, AfterCount, AfterAll, AccumulationMode
from apache_beam.testing.test_pipeline import TestPipeline
from apache_beam.testing.test_stream import TestStream
from apache_beam.testing.util import assert_that, equal_to
import apache_beam as beam

def composite_trigger_afterall_discarding():
    with TestPipeline() as p:
        test_stream = (
            TestStream()
            .advance_watermark_to(0)
            .add_elements(["a", "a", "b"])  # 3 elements in [0,10) window
            .add_elements(["a"])
            .advance_watermark_to(10)
            .advance_watermark_to_infinity()
        )

        trigger = AfterAll(AfterWatermark(), AfterCount(3))

        result = (
            p
            | test_stream
            | beam.Map(lambda x: (x, 1))
            | beam.WindowInto(
                FixedWindows(10),
                trigger=trigger,
                accumulation_mode=AccumulationMode.DISCARDING
            )
            | beam.CombinePerKey(sum)
        )

        # Because of discarding mode, expect multiple partial panes across triggers.
        # So output will be partial counts, possibly multiple panes:
        # This simple test expects at least the final pane sums:
        assert_that(result, equal_to([("a", 3)]))

if __name__ == "__main__":
    composite_trigger_afterall_discarding()
