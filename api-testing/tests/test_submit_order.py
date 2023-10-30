import unittest

from requests_folder.simple_books_requests import submit_an_order


class TestSubmitOrder(unittest.TestCase):

    def test_submit_valid_order(self):
        response = submit_an_order(1, "TMTA7")

        self.assertEqual(response.status_code, 201, "Unexpected status code")
        self.assertTrue(response.json()["created"], "'Created' is not True")

    def test_submit_order_with_invalid_book_id(self):
        book_id = 14
        customer_name = "TMTA7"

        response = submit_an_order(book_id, customer_name)

        expected_error_message = "Invalid or missing bookId."
        actual_error_message = response.json()["error"]

        self.assertEqual(response.status_code, 400, "Unexpected status code")
        self.assertEqual(expected_error_message, actual_error_message, "Unexpected error message")
