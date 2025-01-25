import unittest

class InclusionTests(unittest.TestCase):
    def test_inclusion(self):
        self.assertIn("k", "king", "Error msg")
        self.assertIn(1, [1, 2, 3])
        self.assertIn("a", {"a": 1, "b": 2})
        self.assertIn("a", {"a": 1, "b": 2}.keys())

    def test_non_inclusion(self):
        self.assertNotIn("w", "king")
        self.assertNotIn("a", {"a": 1, "b": 2}.values())

if __name__ == '__main__':
    unittest.main()
