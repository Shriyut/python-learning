from apache_beam.transforms.trigger import AfterCount, Repeatedly
import apache_beam as beam
from apache_beam.transforms.window import FixedWindows
from apache_beam.transforms.trigger import AfterWatermark, AccumulationMode
from apache_beam.testing.test_pipeline import TestPipeline
from apache_beam.testing.test_stream import TestStream
from apache_beam.testing.util import assert_that, equal_to

def after_count_accumulating():
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
                trigger=Repeatedly(AfterCount(2)),
                accumulation_mode=AccumulationMode.ACCUMULATING)
            | beam.CombinePerKey(sum)
        )

        # Because accumulation mode accumulates previous counts:
        # Multiple panes contain increasing sums; final output at least:
        # 'a' count 2 and 'b' count 2
        # Output may contain multiple panes with growing counts; this test checks final total
        assert_that(result, equal_to([('a', 2), ('b', 2)]))

if __name__ == "__main__":
    after_count_accumulating()
