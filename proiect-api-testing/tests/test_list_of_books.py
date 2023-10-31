import unittest

from requests_folder.simple_books_requests import get_list_of_books


class TestListOfBooks(unittest.TestCase):

    def test_get_list_of_books_status_coded(self):
        response = get_list_of_books()
        self.assertEqual(response.status_code, 200, "Unexpected status code")

    def test_get_list_of_books_number_of_results_without_filter(self):
        response = get_list_of_books()

        expected_number_of_results = 6
        actual_number_of_result = len(response.json())

        self.assertEqual(expected_number_of_results, actual_number_of_result, "Unexpected number of results")

        # in cazul in care nu stim neaparat cate raspunsuri vin, dar stim ca trebuie sa fie macar unul
        # self.assertTrue(actual_number_of_result > 1)

    def test_get_list_of_books_filter_by_valid_limit(self):
        response = get_list_of_books(limit=3)

        expected_number_of_results = 3
        actual_number_of_result = len(response.json())

        self.assertEqual(expected_number_of_results, actual_number_of_result, "Expected number of results is not 3")

    def test_get_list_of_books_filter_by_invalid_limit_greater_than_20(self):
        response = get_list_of_books(limit=21)

        expected_status_code = 400
        actual_status_code = response.status_code

        self.assertEqual(expected_status_code, actual_status_code, "Unexpected status code")

        expected_error_message = "Invalid value for query parameter 'limit'. Cannot be greater than 20."
        actual_error_message = response.json()["error"]

        self.assertEqual(expected_error_message, actual_error_message, "Unexpected error message")

    def test_get_list_of_books_filter_by_type_fiction(self):
        self.verify_book_by_type("fiction")

    def test_get_list_of_books_filter_by_type_non_fiction(self):
        self.verify_book_by_type("non-fiction")

    # Deoarece atunci cand testam dupa type (fiction si non-fiction) codul este aproape identic
    # am scos totul intr-o functie in care se schimba doar "book_type" si am apelat functia
    # in cele doua teste de mai sus
    def verify_book_by_type(self, book_type):
        response = get_list_of_books(book_type=book_type)

        expected_status_code = 200
        actual_status_code = response.status_code
        self.assertEqual(expected_status_code, actual_status_code, "Unexpected status code")

        list_of_books = response.json()

        for book in list_of_books:
            print(book['name'])
            assert book['type'] == book_type
