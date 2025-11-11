import apache_beam as beam
from apache_beam.transforms.window import SlidingWindows
from apache_beam.transforms.trigger import AfterWatermark, AccumulationMode
from apache_beam.testing.test_pipeline import TestPipeline
from apache_beam.testing.test_stream import TestStream
from apache_beam.testing.util import assert_that, equal_to, contains_in_any_order

def streaming_wordcount_sliding_window_final_trigger():
    with TestPipeline() as p:
        # Simulated streaming data with timestamps controlled by watermark advances.
        test_stream = (
            TestStream()
            .advance_watermark_to(0)
            .add_elements(["beam", "streaming", "beam"])  # Elements near timestamp 0
            .advance_watermark_to(5)
            .add_elements(["streaming", "test"])  # Elements near timestamp 5
            .advance_watermark_to(20)  # Final watermark to close windows
            .advance_watermark_to_infinity()  # Mark end of input
        )

        # Define sliding windows of 10 seconds length, sliding every 5 seconds.
        # Because of sliding, events may belong to multiple windows.
        # Use AfterWatermark trigger: fires only once when watermark passes window end.
        # Use Discarding accumulation: panes do not accumulate, so one output per window.
        result = (
            p
            | 'Read test stream' >> test_stream
            | 'Split words' >> beam.FlatMap(lambda x: x.split())
            | 'Window into sliding windows' >> beam.WindowInto(
                SlidingWindows(size=10, period=5),
                trigger=AfterWatermark(),
                accumulation_mode=AccumulationMode.DISCARDING
            )
            | 'Pair with one' >> beam.Map(lambda w: (w, 1))
            | 'Count per key' >> beam.CombinePerKey(sum)
        )

        # Assert final outputs for keys with combined counts.
        # Because of sliding windows overlapping, keys may appear multiple times
        # but the test here expects a combined output with these counts somewhere in the results.
        expected_results = [
            ("beam", 2),      # "beam" occurs twice in early elements
            ("streaming", 2), # "streaming" occurs twice at different timestamps
            ("test", 1)
        ]

        # equal_to results in below assertion error
        # apache_beam.testing.util.BeamAssertException: Failed assert: [('beam', 2), ('streaming', 2), ('test', 1)] == [('beam', 2), ('beam', 2), ('streaming', 2), ('streaming', 1), ('streaming', 1), ('test', 1), ('test', 1)], unexpected elements [('beam', 2), ('streaming', 1), ('streaming', 1), ('test', 1)] [while running 'assert_that/Match']
        # this is because each event belongs to multiple overlapping sliding windows ( size = 10s, period = 5s means windows overlap by 5 seconds)
        # output includes counts from all tehse overlapping windows so keys like beam, streaming, and test appear multiple times
        # once per window pane they belong to
        # the assertion expects a single combined output with one entry per key ( as seen in fixed windows)
        # the actual output has multiple entries because of multiple windows firing separately
        # assert_that(result, equal_to(expected_results))

        expected = [
            ("beam", 2), ("beam", 2),  # beam appears in 2 overlapping windows
            ("streaming", 2), ("streaming", 1), ("streaming", 1),
            ("test", 1), ("test", 1)
        ]
        # assert_that(result, contains_in_any_order(expected))  # causes callable type error
        assert_that(result, contains_in_any_order([
            ("beam", 2), ("beam", 2),  # beam appears in 2 overlapping windows
            ("streaming", 2), ("streaming", 1), ("streaming", 1),
            ("test", 1), ("test", 1)
        ]))

if __name__ == '__main__':
    streaming_wordcount_sliding_window_final_trigger()
