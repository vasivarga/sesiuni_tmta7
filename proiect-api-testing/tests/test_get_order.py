import unittest

from requests_folder.simple_books_requests import submit_an_order, get_an_order


class TestGetOrder(unittest.TestCase):

    def test_get_an_order(self):
        # Ca sa putem lua o comanda, este nevoie sa plasam una noua
        submit_order_response = submit_an_order(1, "tmta7")
        
        order_id = submit_order_response.json()["orderId"]

        get_order_response = get_an_order(order_id)

        self.assertEqual(get_order_response.status_code, 200, "Unexpected status code")
        self.assertEqual(get_order_response.json()["bookId"], 1, "Unexpected book id")
        self.assertEqual(get_order_response.json()["customerName"], "tmta7", "Unexpected customer name")
