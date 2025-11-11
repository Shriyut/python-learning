import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

def run_pipeline(p=None):
    # Parse pipeline arguments (these can come from sys.argv, argparse, YAML, or env vars)
    options = PipelineOptions(
        runner='DirectRunner',
        save_main_session=True
    )

    p = p or beam.Pipeline(options=options)

    # with beam.Pipeline(options=options) as p:
    #     (
    #         p
    #         | 'CreateNumbers' >> beam.Create([1, 2, 3, 4, 5])
    #         | 'MultiplyBy10' >> beam.Map(lambda x: x * 10)
    #         | 'PrintResults' >> beam.Map(print)
    #     )

    output = (
            p
            | 'CreateNumbers' >> beam.Create([1, 2, 3, 4, 5])
            | 'MultiplyBy10' >> beam.Map(lambda x: x * 10)
    )

    _ = output | 'PrintOutput' >> beam.Map(print)

    # if p._is_running_in_context_manager:  # When using with block, do not call run again
    #     return output
    # else:
    p.run().wait_until_finish()
    return output
