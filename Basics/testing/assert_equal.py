import unittest

class TestStringMethods(unittest.TestCase):
    def test_split(self):
        #  test cases should start with test keyword
        self.assertEqual("a-b-c".split("-"), ["a", "b", "c"])
        self.assertEqual("d+e+f".split("+"), ["d", "e", "f"])

    def test_count(self):
        self.assertEqual("beautiful".count("z"), 2) # raises Assertion Error


if __name__ == "__main__":
    unittest.main()