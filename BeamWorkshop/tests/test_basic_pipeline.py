import unittest
import apache_beam as beam
from apache_beam.testing.test_pipeline import TestPipeline
from apache_beam.testing.util import assert_that, equal_to

from pipeline_resources import pipeline_launcher


class BasicPipelineTest(unittest.TestCase):
    # def test_multiply_by_10(self):
    #     test_input = [1, 2, 3, 4, 5]
    #     expected_output = [10, 20, 30, 40, 50]
    #     with TestPipeline() as p:
    #         result = (
    #             p
    #             | 'CreateTestInput' >> beam.Create(test_input)
    #             | 'MultiplyBy10' >> beam.Map(lambda x: x * 10)
    #         )
    #         assert_that(result, equal_to(expected_output))

    def test_run_pipeline(self):
        with TestPipeline() as p:
            result = pipeline_launcher.run_pipeline(p)
            assert_that(result, equal_to([10, 20, 30, 40, 50]))

if __name__ == "__main__":
    unittest.main()