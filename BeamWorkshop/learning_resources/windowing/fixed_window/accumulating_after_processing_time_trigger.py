from apache_beam.transforms.trigger import AfterProcessingTime
import apache_beam as beam
from apache_beam.transforms.window import FixedWindows
from apache_beam.transforms.trigger import AfterWatermark, AccumulationMode
from apache_beam.testing.test_pipeline import TestPipeline
from apache_beam.testing.test_stream import TestStream
from apache_beam.testing.util import assert_that, equal_to

def after_processing_time_accumulating():
    with TestPipeline() as p:
        test_stream = (
            TestStream()
            .advance_watermark_to(0)
            .add_elements(['a', 'b'])
            .advance_processing_time(3000)  # Advance processing time (e.g., 3 seconds)
            .add_elements(['a'])
            .advance_watermark_to(10)
            .advance_watermark_to_infinity()
        )

        result = (
            p
            | test_stream
            | beam.Map(lambda x: (x, 1))
            | beam.WindowInto(
                FixedWindows(10),
                trigger=AfterProcessingTime(delay=3000),
                accumulation_mode=AccumulationMode.ACCUMULATING)
            | beam.CombinePerKey(sum)
        )

        assert_that(result, equal_to([('a', 2), ('b', 1)]))

if __name__ == "__main__":
    after_processing_time_accumulating()
