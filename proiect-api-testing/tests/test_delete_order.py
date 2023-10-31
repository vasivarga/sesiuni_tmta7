import unittest

from requests_folder.simple_books_requests import submit_an_order, delete_an_order, update_an_order


class TestDeleteOrder(unittest.TestCase):

    def test_delete_order_status_code(self):
        # Ca sa putem sterge o comanda, este nevoie sa plasam una noua
        book_id = 1
        customer_name = "TMTA7_ORDER"

        submit_order_response = submit_an_order(book_id, customer_name)
        order_id = submit_order_response.json()["orderId"]

        delete_order_response = delete_an_order(order_id)

        expected_status_code = 204
        actual_status_code = delete_order_response.status_code

        self.assertEqual(expected_status_code, actual_status_code, "Unexpected status code")

