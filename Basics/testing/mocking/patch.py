"""Patch can be used as a function or a decorator that will create a magicmock object for us"""
# patch intercepts a call to object and places the magic mock object

import urllib.request
import unittest
from unittest.mock import patch

class WebRequest:
    def __init__(self, url):
        self.url = url

    def execute(self):
        response = urllib.request.urlopen(self.url)
        if response.status == 200:
            return "Success"

        return "Failure"

# wr = WebRequest("https://www.google.com")
# wr.execute()

# from webrequest import WebRequest - if the below test case was in another file in the same location
# @patch('web_request.urlopen')
# from urllib.request import urlopen in web_request file
class WebRequestTest(unittest.TestCase):
    def test_success(self):
        # with patch('package.module.attribute')
        with patch('urllib.request.urlopen') as mock_urlopen:
            mock_urlopen.return_value.status = 200
            wr = WebRequest("https://www.google.com")
            self.assertEqual(wr.execute(), "Success")

    def test_failure(self):
        with patch('urllib.request.urlopen') as mock_urlopen:
            mock_urlopen.return_value.status = 404
            wr = WebRequest("http://www.asdadasd.com")
            self.assertEqual(wr.execute(), "Failure")

    @patch('urllib.request.urlopen')
    def test_success_patch_decorator(self, mock_urlopen):
        mock_urlopen.return_value.status = 200
        wr = WebRequest("https://www.google.com")
        self.assertEqual(wr.execute(), "Success")

    @patch('urllib.request.urlopen')
    def test_failure_patch_decorator(self, mock_urlopen):
        mock_urlopen.return_value.status = 404
        wr = WebRequest("http://www.asdadasd.com")
        self.assertEqual(wr.execute(), "Failure")


if __name__ == "__main__":
    unittest.main()