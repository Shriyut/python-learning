import unittest
from unittest.mock import MagicMock

class MockCallsTest(unittest.TestCase):
    def test_mock_calls(self):
        mock = MagicMock()
        # mock()
        mock()
        mock.assert_called() # throws AssertionError if mock() is commented

    def test_not_called(self):
        mock = MagicMock()
        mock.assert_not_called() # throws error if mock object is called

    def test_called_with(self):
        mock = MagicMock()
        mock(1, 2, 3)
        # mock.assert_called_with(1, 2) # throws an error
        mock.assert_called_with(1, 2, 3)

    def test_mock_attributes(self):
        mock = MagicMock()
        mock()
        mock(1, 2)
        print(mock.called) # true
        print(mock.call_count) # 2
        print(mock.mock_calls) 

if __name__ == "__main__":
    unittest.main()