import apache_beam as beam
from apache_beam.transforms.window import Sessions
from apache_beam.testing.test_pipeline import TestPipeline
from apache_beam.testing.test_stream import TestStream
from apache_beam.testing.util import assert_that, equal_to
from apache_beam.utils.timestamp import Timestamp

def session_window_test():
    with TestPipeline() as p:
        # Create a TestStream of elements with explicit event timestamps
        test_stream = (
            TestStream()
            .add_elements([
                beam.window.TimestampedValue('a', 1),
                beam.window.TimestampedValue('b', 2),
                beam.window.TimestampedValue('a', 10),
            ])
            .advance_watermark_to(15)
            .advance_watermark_to_infinity()
        )

        # Session windows with 5-second gap duration
        result = (
            p
            | test_stream
            | beam.Map(lambda x: (x, 1))
            | beam.WindowInto(Sessions(gap_size=5))
            | beam.CombinePerKey(sum)
        )

        # Expected: elements 'a' at time 1 and 'a' at 10 form separate sessions(count=1 each),
        # 'b' at time 2 forms its own session
        expected = [
            ('a', 1),
            ('b', 1),
            ('a', 1),
        ]

        assert_that(result, equal_to(expected))

if __name__ == "__main__":
    session_window_test()
