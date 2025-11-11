from apache_beam.testing.test_stream import TestStream
from apache_beam.testing.test_pipeline import TestPipeline
from apache_beam.testing.util import assert_that, equal_to
from apache_beam.transforms.trigger import AccumulationMode
from apache_beam.transforms.window import FixedWindows
import apache_beam as beam


def streaming_wordcount_with_complete_watermark():
    with TestPipeline() as p:
        # TestStream with watermark advances beyond last window to ensure all panes are fired
        test_stream = (
            TestStream()
            .advance_watermark_to(0)
            .add_elements(["beam", "streaming", "beam"])
            .advance_watermark_to(5)
            .add_elements(["streaming", "test"])
            .advance_watermark_to(20)  # Past end of 10-sec fixed windows to fire all panes
            .advance_watermark_to_infinity()
        )

        # watermark advances as follows
        # at 0 - first batch of elements ("beam", "streaming", "beam") arrive
        # since no early or late triggers are set, teh default trigger - AfterWatermark ( fires once when watermark passes window end)
        # with watermark advancing beyond window ends only once, each window will fire exactly one pane ( the final pane)
        # total panes fired = number of windows emitting results
        # in this example 2 panes - 1 per window
        # each pane contains aggregated counts for that window
        # accumulation mode allows counts to build over multiple firings if early triggers are used
        # here only one firing per window
        result = (
                p
                | test_stream
                | beam.FlatMap(lambda x: x.split())
                | beam.WindowInto(
                    FixedWindows(10),
                    accumulation_mode=AccumulationMode.ACCUMULATING)
                | beam.Map(lambda w: (w, 1))
                | beam.CombinePerKey(sum)
        )

        _ = result | "Print" >> beam.Map(print)

        assert_that(result, equal_to([("beam", 2), ("streaming", 2), ("test", 1)]))


if __name__ == '__main__':
    streaming_wordcount_with_complete_watermark()
