import requests
from generate_token_request import generate_token

token = generate_token()


def submit_an_order():
    header = {'Authorization': token}
    data_body = {
        "bookId": 1,
        "customerName": "John"
    }
    response = requests.post('https://simple-books-api.glitch.me/orders', headers=header, json=data_body)
    return response


# print(submit_an_order())
# print(submit_an_order().json())
# print(submit_an_order().json()['orderId'])

def get_an_order(orderId):
    header = {'Authorization': token}
    response = requests.get(f'https://simple-books-api.glitch.me/orders/{orderId}',headers=header)
    return response


order_id = submit_an_order().json()['orderId']


# print(get_an_order(order_id))
# print(get_an_order(order_id).json())

def update_an_order(orderId):
    header = {'Authorization': token}
    data_body = {
        "customerName": "Diana"
    }
    response = requests.patch(f'https://simple-books-api.glitch.me/orders/{orderId}',
                              headers=header, json=data_body)
    return response
# print(update_an_order(order_id))

def delete_an_order(orderId):
    header = {'Authorization': token}
    response = requests.delete(f'https://simple-books-api.glitch.me/orders/{orderId}',
                               headers=header)
    return response
# print(delete_an_order(order_id))

def get_all_orders():
    header = {'Authorization': token}
    response = requests.get('https://simple-books-api.glitch.me/orders', headers=header)
    return response
# print(get_all_orders())

def get_a_single_book(bookId):
    response = requests.get(f'https://simple-books-api.glitch.me/books/{bookId}')
    return response
# print(get_a_single_book(4))

def get_list_of_books():
    response = requests.get('https://simple-books-api.glitch.me/books')
    return response
# print(get_list_of_books())

def get_list_of_books(type, limit):
    response = requests.get(f'https://simple-books-api.glitch.me/books?type={type}&limit={limit}')
    return response
# print(get_list_of_books('fiction', 14))
# print(get_list_of_books('fiction', 14).json())

def api_status():
    response = requests.get('https://simple-books-api.glitch.me/status')
    return response
print(api_status())