"""
This pipeline emits partial sums every 3 elements in a window, accumulating results across triggers, demonstrating early and final output.
"""

import apache_beam as beam
from apache_beam.transforms.window import FixedWindows
from apache_beam.transforms.trigger import AfterCount, Repeatedly, AccumulationMode

with beam.Pipeline() as p:
    (p
     | 'CreateData' >> beam.Create([1,2,3,4,5,6])
     | 'ApplyWindow' >> beam.WindowInto(
         FixedWindows(10),
         trigger=Repeatedly(AfterCount(3)),  # fires after each 3 elements
         accumulation_mode=AccumulationMode.ACCUMULATING)  # accumulate results
     | 'Sum' >> beam.CombineGlobally(sum).without_defaults()
     | 'print' >> beam.Map(print))
