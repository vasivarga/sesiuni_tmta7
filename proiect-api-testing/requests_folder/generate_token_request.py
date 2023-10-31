from random import randint

import requests


def generate_token():
    random_number = randint(1, 99999999999999)
    data_body = {
        "clientName": "Diana",
        "clientEmail": f"diana{random_number}@example.com"
    }
    response = requests.post('https://simple-books-api.glitch.me/api-clients/', json=data_body)
    return response.json()['accessToken']
