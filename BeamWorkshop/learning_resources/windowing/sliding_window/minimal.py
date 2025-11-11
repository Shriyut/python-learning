import apache_beam as beam
from apache_beam.testing.test_pipeline import TestPipeline
from apache_beam.testing.util import assert_that, contains_in_any_order

# with TestPipeline() as p:
#     pcoll = p | beam.Create([("foo", 1), ("bar", 2), ("foo", 3)])
#
#     def sum_values(elements):
#         key, values = elements
#         return (key, sum(values))
#
#     counted = (pcoll
#                | beam.GroupByKey()
#                | beam.Map(sum_values))
#
#     expected = [("foo", 4), ("bar", 2)]
#
#     assert_that(counted, contains_in_any_order(expected))

# import apache_beam as beam
# from apache_beam.testing.test_pipeline import TestPipeline
# from apache_beam.testing.util import assert_that
from collections import Counter

def aggregate_key_counts(elements):
    """
    Custom matcher callable for assert_that that aggregates counts per key.
    Input: list of (key, count) tuples, may include duplicates.
    Output: asserts equality of aggregated counts against expected.
    """
    def matcher(actual):
        # actual is an iterable of (key, count)
        actual_counter = Counter()
        for k, v in actual:
            actual_counter[k] += v
        expected_counter = Counter()
        for k, v in elements:
            expected_counter[k] += v
        assert actual_counter == expected_counter, (
            f"Mismatch:\nActual: {actual_counter}\nExpected: {expected_counter}")
    return matcher

def minimal_test_with_custom_matcher():
    with TestPipeline() as p:
        pcoll = p | beam.Create([("foo", 1), ("bar", 2), ("foo", 3)])

        def sum_values(kv):
            key, values = kv
            return (key, sum(values))

        counted = (
            pcoll
            | beam.GroupByKey()
            | beam.Map(sum_values)
        )

        expected = [("foo", 4), ("bar", 2)]

        # Pass the custom matcher callable to assert_that
        assert_that(counted, aggregate_key_counts(expected))

if __name__ == "__main__":
    minimal_test_with_custom_matcher()
