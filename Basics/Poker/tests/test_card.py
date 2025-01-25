import unittest

class CardTest(unittest.TestCase):
    def test_setup(self):
        self.assertEqual(1, 1)

# python3 -m unittest discover tests
#  if executed from parent poker folder
# python3 -m unittest tests/test_card.py