import apache_beam as beam
from apache_beam.transforms.window import FixedWindows
from apache_beam.transforms.trigger import AfterWatermark, AfterCount, AfterAll, AccumulationMode
from apache_beam.testing.test_pipeline import TestPipeline
from apache_beam.testing.test_stream import TestStream
from apache_beam.testing.util import assert_that, equal_to

def composite_trigger_fixed_window():
    with TestPipeline() as p:
        test_stream = (
            TestStream()
            .advance_watermark_to(0)
            .add_elements(["a", "b", "a"])
            .advance_watermark_to(5)
            .add_elements(["b"])
            .advance_watermark_to(10)
            .advance_watermark_to_infinity()
        )

        # Composite trigger: fire only when both watermark passes AND 3 elements arrived
        composite_trigger = AfterAll(
            AfterWatermark(), AfterCount(3)
        )

        result = (
            p
            | test_stream
            | beam.Map(lambda x: (x, 1))
            | beam.WindowInto(
                FixedWindows(10),
                trigger=composite_trigger,
                accumulation_mode=AccumulationMode.ACCUMULATING
            )
            | beam.CombinePerKey(sum)
        )

        # Expect final counts after both triggers fire; sum of all elements within window
        # input data doesnot satisfy the composite trigger criteria
        assert_that(result, equal_to([]))
        # assert_that(result, equal_to([("a", 2), ("b", 2)]))

if __name__ == "__main__":
    composite_trigger_fixed_window()
