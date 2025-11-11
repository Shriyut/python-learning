import logging
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions, StandardOptions
from apache_beam.transforms.window import FixedWindows
import re
import time
from apache_beam import DoFn, ParDo, Create, WindowInto
from apache_beam.utils.timestamp import Timestamp

logging.basicConfig(level=logging.INFO)

class SplitWordsFn(beam.DoFn):
    def process(self, element):
        words = re.findall(r'\w+', element)
        for word in words:
            yield word

class EmitLinesWithTimestamp(DoFn):
    def __init__(self, lines, interval_sec=1):
        self.lines = lines
        self.interval_sec = interval_sec

    def process(self, unused_element, timestamp=DoFn.TimestampParam):
        # Emit lines with assigned event-time timestamps incremented by interval
        for i, line in enumerate(self.lines):
            yield beam.window.TimestampedValue(line, Timestamp(i * self.interval_sec))

def run():
    options = PipelineOptions()
    options.view_as(StandardOptions).streaming = True

    p = beam.Pipeline(options=options)

    # Read file lines once outside pipeline
    with open('/home/sunny/PycharmProjects/python-learning/BeamWorkshop/resources/lorem.txt') as f:
        file_lines = [line.strip() for line in f if line.strip()]

    # Create a dummy PCollection with a single element to trigger line emission
    input_trigger = p | 'CreateOne' >> Create([None])

    # Emit lines as if streaming, assigning incremental timestamps
    lines = input_trigger | 'EmitLines' >> ParDo(EmitLinesWithTimestamp(file_lines, interval_sec=1))

    windowed = lines | 'FixedWindow' >> WindowInto(FixedWindows(10))

    words = windowed | 'SplitWords' >> ParDo(SplitWordsFn())

    pairs = words | 'PairWithOne' >> beam.Map(lambda w: (w, 1))

    counts = pairs | 'CountWords' >> beam.CombinePerKey(sum)

    formatted = counts | 'FormatResults' >> beam.Map(lambda kv: f'{kv[0]}: {kv[1]}')

    formatted | 'PrintResults' >> beam.Map(lambda line: logging.info(f'Line: {line}') or line)

    formatted | 'WriteOutput' >> beam.io.WriteToText('/home/sunny/PycharmProjects/python-learning/BeamWorkshop/resources/tmp/lorem_wordcount_streaming',
                                                    file_name_suffix='.txt',
                                                    shard_name_template='')

    result = p.run()
    result.wait_until_finish()

if __name__ == '__main__':
    run()
