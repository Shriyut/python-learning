import logging
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
import re

class SplitWordsFn(beam.DoFn):
    def process(self, element):
        words = re.findall(r'\w+', element)
        for word in words:
            yield word

def run():
    logging.basicConfig(level=logging.INFO)

    options = PipelineOptions([
        '--runner=DirectRunner',
        '--experiments=use_legacy_direct_runner'
    ])

    p = beam.Pipeline(options=options)

    lines = p | 'ReadLines' >> beam.io.ReadFromText('/home/sunny/PycharmProjects/python-learning/BeamWorkshop/resources/lorem.txt')

    words = lines | 'SplitWords' >> beam.ParDo(SplitWordsFn())

    pairs = words | 'PairWithOne' >> beam.Map(lambda w: (w, 1))

    counts = pairs | 'CountWords' >> beam.CombinePerKey(sum)

    formatted = counts | 'FormatResults' >> beam.Map(lambda kv: f'{kv[0]}: {kv[1]}')

    formatted | 'PrintResults' >> beam.Map(lambda line: logging.info(f'Line: {line}') or line)

    formatted | 'WriteOutput' >> beam.io.WriteToText('/home/sunny/PycharmProjects/python-learning/BeamWorkshop/resources/tmp/lorem_wordcount',
                                                     file_name_suffix='.txt',
                                                     shard_name_template=''
                                                     )

    result = p.run()
    result.wait_until_finish()

if __name__ == '__main__':
    run()
