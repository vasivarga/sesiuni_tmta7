import unittest

from requests_folder.simple_books_requests import get_api_status


class TestApiStatus(unittest.TestCase):

    def test_api_status_code(self):
        response = get_api_status()
        self.assertEqual(response.status_code, 200, "Unexpected status code")

    def test_api_status_message(self):
        response = get_api_status()
        self.assertEqual(response.json()["status"], "OK", "Unexpected status message")

    