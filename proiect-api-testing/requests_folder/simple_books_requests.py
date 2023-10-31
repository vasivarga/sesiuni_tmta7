import requests

from requests_folder.generate_token_request import generate_token

token = generate_token()


def submit_an_order(book_id, customer_name):
    header = {'Authorization': token}
    data_body = {
        "bookId": book_id,
        "customerName": customer_name
    }
    response = requests.post('https://simple-books-api.glitch.me/orders', headers=header, json=data_body)
    return response


def get_an_order(order_id):
    header = {'Authorization': token}
    response = requests.get(f'https://simple-books-api.glitch.me/orders/{order_id}', headers=header)
    return response


def update_an_order(order_id, new_name):
    header = {'Authorization': token}
    data_body = {
        "customerName": new_name
    }
    response = requests.patch(f'https://simple-books-api.glitch.me/orders/{order_id}',
                              headers=header, json=data_body)
    return response


def delete_an_order(order_id):
    header = {'Authorization': token}
    response = requests.delete(f'https://simple-books-api.glitch.me/orders/{order_id}', headers=header)
    return response


def get_all_orders():
    header = {'Authorization': token}
    response = requests.get('https://simple-books-api.glitch.me/orders', headers=header)
    return response


def get_a_single_book(book_id):
    response = requests.get(f'https://simple-books-api.glitch.me/books/{book_id}')
    return response


def get_list_of_books(book_type="", limit=""):
    response = requests.get(f'https://simple-books-api.glitch.me/books?type={book_type}&limit={limit}')
    return response


def get_api_status():
    response = requests.get('https://simple-books-api.glitch.me/status')
    return response
