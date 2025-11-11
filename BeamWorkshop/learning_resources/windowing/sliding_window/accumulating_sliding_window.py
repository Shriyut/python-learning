import apache_beam as beam
from apache_beam.transforms.window import SlidingWindows
from apache_beam.transforms.trigger import AfterCount, Repeatedly, AccumulationMode
from apache_beam.testing.test_pipeline import TestPipeline
from apache_beam.testing.test_stream import TestStream
from apache_beam.testing.util import assert_that, equal_to

def streaming_wordcount_with_sliding_window():
    with TestPipeline() as p:
        test_stream = (
            TestStream()
            .advance_watermark_to(0)
            .add_elements([
                "beam", "streaming", "beam"  # Events around timestamp 0
            ])
            .advance_watermark_to(5)
            .add_elements([
                "streaming", "test"  # Events arriving near timestamp 5
            ])
            .advance_watermark_to(10)
            .add_elements([
                "extra", "elements", "for", "more", "windows"  # Events at timestamp 10
            ])
            .advance_watermark_to(15)
            .add_elements([
                "even", "more", "data"  # Events around timestamp 15
            ])
            .advance_watermark_to(25)  # Move watermark past last window end to finalize firing
            .advance_watermark_to_infinity()  # Signal end of stream
        )

        # Sliding window of size 10 seconds, sliding every 5 seconds:
        # Each event belongs to 2 overlapping windows, e.g.,
        # an event at timestamp 4 belongs to windows: [0-10) and [5-15)
        result = (
            p
            | test_stream
            | beam.FlatMap(lambda x: x.split())
            | beam.WindowInto(
                SlidingWindows(size=10, period=5),  # 10s window sliding every 5s
                trigger=Repeatedly(AfterCount(2)),  # Early firing after every 2 elements
                accumulation_mode=AccumulationMode.ACCUMULATING  # Accumulate counts in multiple panes
            )
            | beam.Map(lambda w: (w, 1))
            | beam.CombinePerKey(sum)
        )

        # The output will have counts combined for events spread over multiple overlapping windows,
        # and multiple firings per window due to the trigger.
        # Here, we check final aggregated counts in any window.
        assert_that(result, equal_to([
            ("beam", 2),
            ("streaming", 2),
            ("test", 1),
            ("extra", 1),
            ("elements", 1),
            ("for", 1),
            ("more", 2),    # "more" appears twice in data
            ("windows", 1),
            ("even", 1),
            ("data", 1)
        ]))

if __name__ == '__main__':
    streaming_wordcount_with_sliding_window()