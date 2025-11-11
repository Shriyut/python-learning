import apache_beam as beam
from apache_beam.transforms.window import FixedWindows
from apache_beam.transforms.trigger import AfterWatermark, AfterCount, AfterFirst, AccumulationMode
from apache_beam.testing.test_pipeline import TestPipeline
from apache_beam.testing.test_stream import TestStream
from apache_beam.testing.util import assert_that, equal_to

def composite_trigger_fixed_window_fixed():
    with TestPipeline() as p:
        # TestStream with 3 elements in first window [0,10), watermark advances after
        test_stream = (
            TestStream()
            .advance_watermark_to(0)
            .add_elements(["a", "a", "b"])  # 3 elements, meet count trigger
            .advance_watermark_to(10)        # watermark passes first window end
            .advance_watermark_to_infinity()
        )

        # Composite trigger: fires when either watermark passes or count >=3
        # not supported in python
        composite_trigger = AfterFirst(
            AfterWatermark(),
            AfterCount(3)
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

        # Expect full counts per key since accumulation and early trigger fire
        assert_that(result, equal_to([("a", 2), ("b", 1)]))

if __name__ == "__main__":
    composite_trigger_fixed_window_fixed()
