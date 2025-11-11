import apache_beam as beam
from apache_beam.transforms.window import Sessions
from apache_beam.transforms.trigger import AfterProcessingTime, AfterWatermark, AccumulationMode, AfterCount, Repeatedly
from apache_beam.testing.test_pipeline import TestPipeline
from apache_beam.testing.test_stream import TestStream

def session_window_test_with_triggers():
    with TestPipeline() as p:
        test_stream = (
            TestStream()
            .add_elements([
                beam.window.TimestampedValue('a', 1),
                beam.window.TimestampedValue('b', 2),
                beam.window.TimestampedValue('a', 10),
                beam.window.TimestampedValue('a', 12),
                beam.window.TimestampedValue('b', 13),
            ])
            .advance_watermark_to(20)
            .advance_watermark_to_infinity()
        )

        # 1) Default trigger (AfterWatermark with default early firings)
        default_trigger_result = (
            test_stream
            | "DefaultTriggerMap" >> beam.Map(lambda x: (x, 1))
            | "DefaultTriggerWindow" >> beam.WindowInto(Sessions(gap_size=5))
            | "DefaultTriggerSum" >> beam.CombinePerKey(sum)
        )

        # 2) Trigger: After watermark passes end-of-window, with early firings every 3 seconds processing time
        early_trigger_result = (
            test_stream
            | "EarlyTriggerMap" >> beam.Map(lambda x: (x, 1))
            | "EarlyTriggerWindow" >> beam.WindowInto(
                Sessions(gap_size=5),
                trigger=AfterWatermark(),
                accumulation_mode=AccumulationMode.DISCARDING)
            | "EarlyTriggerSum" >> beam.CombinePerKey(sum)
        )

        # 3) Trigger: Repeatedly after count of 2 elements in pane
        count_trigger_result = (
            test_stream
            | "CountTriggerMap" >> beam.Map(lambda x: (x, 1))
            | "CountTriggerWindow" >> beam.WindowInto(
                Sessions(gap_size=5),
                trigger=Repeatedly(AfterCount(2)),
                accumulation_mode=AccumulationMode.ACCUMULATING)
            | "CountTriggerSum" >> beam.CombinePerKey(sum)
        )

        # 4) Trigger: After watermark, late firing allowed 5 seconds processing time
        late_trigger_result = (
            test_stream
            | "LateTriggerMap" >> beam.Map(lambda x: (x, 1))
            | "LateTriggerWindow" >> beam.WindowInto(
                Sessions(gap_size=5),
                trigger=AfterWatermark(late=AfterProcessingTime(5)),
                accumulation_mode=AccumulationMode.DISCARDING)
            | "LateTriggerSum" >> beam.CombinePerKey(sum)
        )

        # Print results (for demonstration purposes)
        default_trigger_result | "PrintDefault" >> beam.Map(print)
        early_trigger_result | "PrintEarly" >> beam.Map(print)
        count_trigger_result | "PrintCount" >> beam.Map(print)
        late_trigger_result | "PrintLate" >> beam.Map(print)

        result = (
                p
                | test_stream
                | beam.Map(lambda x: (x, 1))
                | beam.WindowInto(
                    Sessions(gap_size=5),
                    trigger=AfterCount(1),  # early trigger to force output after every element
                    accumulation_mode=AccumulationMode.DISCARDING
                )
                | beam.CombinePerKey(sum)
        )

        result | beam.Map(print)

if __name__ == "__main__":
    session_window_test_with_triggers()
