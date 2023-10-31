import unittest

from requests_folder.simple_books_requests import submit_an_order, update_an_order


class TestUpdateOrder(unittest.TestCase):

    def test_update_order_status_code(self):

        # Ca sa putem modifica o comanda, este nevoie sa plasam una noua
        book_id = 1
        customer_name = "TMTA7_INITIAL"

        submit_order_response = submit_an_order(book_id, customer_name)

        order_id = submit_order_response.json()["orderId"]

        new_customer_name = "TMTA7_UPDATED"

        update_order_response = update_an_order(order_id, new_customer_name)

        expected_status_code = 204
        actual_status_code = update_order_response.status_code
        self.assertEqual(expected_status_code, actual_status_code, "Unexpected status code")
