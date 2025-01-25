import unittest

class TestOperations(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #  create db connection here
        print("THis will run once before the test suite starts")

    def setUp(self):
        print("THis will run before every test case")

    def tearDown(self):
        print("This will run after every test case")

    @classmethod
    def tearDownClass(cls):
        #  close db connection here
        print("THis will run once after the test suite finishes")

    def test_stuff(self):
        self.assertEqual(1, 1)

    def test_more_stuff(self):
        self.assertEqual([], [])

if __name__ == "__main__":
    unittest.main()