import logging
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.transforms.window import FixedWindows
from apache_beam.transforms.trigger import AfterProcessingTime, Repeatedly, AccumulationMode, AfterCount
import re

class SplitWordsFn(beam.DoFn):
    def process(self, element):
        # Tokenize line into words using regex for robust splitting
        words = re.findall(r'\w+', element)
        for word in words:
            # logging.info(word)
            yield word


def run():
    logging.basicConfig(level=logging.INFO)
    options = PipelineOptions([
        '--runner=DirectRunner',
        '--experiments=use_legacy_direct_runner'
    ])

    # Create Pipeline object explicitly
    p = beam.Pipeline(options=options)

    # Apply transforms
    lines = p | 'ReadLines' >> beam.io.ReadFromText('/home/sunny/PycharmProjects/python-learning/BeamWorkshop/resources/lorem.txt')

    lines | 'LogLines' >> beam.Map(lambda line: logging.info(f'Line: {line}') or line)
    # windowed = lines | 'WindowIntoFixed' >> beam.WindowInto(FixedWindows(60))

    windowed = (
            lines
            | 'WindowIntoFixed' >> beam.WindowInto(
        FixedWindows(60),  # 1-minute fixed windows
        trigger=Repeatedly(AfterProcessingTime(0)),  # fire ASAP repeatedly as elements arrive
        accumulation_mode=AccumulationMode.DISCARDING  # discard old pane state on new firing
    )
    )

    words = windowed | 'SplitWords' >> beam.ParDo(SplitWordsFn())

    pairs = words | 'PairWithOne' >> beam.Map(lambda w: (w, 1))

    counts = pairs | 'CountWords' >> beam.CombinePerKey(sum)

    formatted = counts | 'FormatResults' >> beam.Map(lambda kv: f'{kv[0]}: {kv[1]}')

    # Print output (only for debugging in DirectRunner)
    formatted | 'PrintResults' >> beam.Map(lambda line: logging.info(f'Line: {line}') or line)

    formatted | 'WriteOutput' >> beam.io.WriteToText(r'/home/sunny/PycharmProjects/python-learning/BeamWorkshop/resources/tmp/lorem.txt')

    # Explicitly run pipeline and wait until finish
    result = p.run()
    result.wait_until_finish()

if __name__ == '__main__':
    run()
