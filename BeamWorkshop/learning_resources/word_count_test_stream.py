from apache_beam.testing.test_stream import TestStream
from apache_beam.testing.test_pipeline import TestPipeline
from apache_beam.testing.util import assert_that, equal_to
from apache_beam.transforms.trigger import AccumulationMode
from apache_beam.transforms.window import FixedWindows
import apache_beam as beam

def test_streaming_wordcount():
    with TestPipeline() as p:
        test_stream = (
            TestStream()
            .advance_watermark_to(0)
            .add_elements(["beam", "streaming", "beam"])
            .advance_watermark_to(10)
            .add_elements(["streaming", "test"])
            .advance_watermark_to_infinity()
        )

        # result = (
        #     p
        #     | test_stream
        #     | beam.FlatMap(lambda x: x.split())
        #     | beam.Map(lambda w: (w, 1))
        #     | beam.CombinePerKey(sum)
        # )

        result = (
                p
                | test_stream
                | beam.FlatMap(lambda x: x.split())
                | beam.WindowInto(FixedWindows(10))  # Add a fixed window of 10 seconds
                | beam.Map(lambda w: (w, 1))
                | beam.CombinePerKey(sum)
        )


        # below assert fails because of windowing with default accumulation mode of discarding
        # repeated keys arriving in different panes/windows do not get combined into one output element
        # refer to the accumulating_test_streaming_Wordcount method
        # assert_that(result, equal_to([("beam", 2), ("streaming", 2), ("test", 1)]))

        assert_that(result, equal_to([("beam", 2), ("streaming", 1), ("streaming", 1), ("test", 1)]))


def accumulating_test_streaming_wordcount():
    with TestPipeline() as p:
        test_stream = (
            TestStream()
            .advance_watermark_to(0)
            .add_elements(["beam", "streaming", "beam"])
            .advance_watermark_to(10)
            .add_elements(["streaming", "test"])
            .advance_watermark_to_infinity()
        )

        result = (
                p
                | test_stream
                | beam.FlatMap(lambda x: x.split())
                | beam.WindowInto(FixedWindows(10),
                                  accumulation_mode=AccumulationMode.ACCUMULATING)  # Add a fixed window of 10 seconds
                | beam.Map(lambda w: (w, 1))
                | beam.CombinePerKey(sum)
        )
        assert_that(result, equal_to([("beam", 2), ("streaming", 2), ("test", 1)]))


# test_streaming_wordcount()
accumulating_test_streaming_wordcount()