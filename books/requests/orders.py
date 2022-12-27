import requests
from requests.structures import CaseInsensitiveDict


def add_order(token, book_id, customer_name):
    headers = CaseInsensitiveDict()
    headers['Accept'] = 'application/json'
    headers['Authorization'] = f'Bearer {token}'
    json = {
        'bookId': book_id,
        'customerName': customer_name
    }
    response = requests.post(f'https://simple-books-api.glitch.me/orders', headers=headers, json=json)
    return response


def delete_order(token, order_id):
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = f"Bearer {token}"
    response = requests.delete(f'https://simple-books-api.glitch.me/orders/{order_id}', headers=headers)
    return response


def get_orders(token):
    headers = CaseInsensitiveDict()
    headers['Accept'] = 'application/json'
    headers['Authorization'] = f'Bearer {token}'
    response = requests.get(f'https://simple-books-api.glitch.me/orders/', headers=headers)
    return response


def get_order(token, order_id):
    headers = CaseInsensitiveDict()
    headers['Accept'] = 'application/json'
    headers['Authorization'] = f'Bearer {token}'
    response = requests.get(f'https://simple-books-api.glitch.me/orders/{order_id}', headers=headers)
    return response


def edit_order(token, order_id, customer_name):
    headers = CaseInsensitiveDict()
    headers['Accept'] = 'application/json'
    headers['Authorization'] = f'Bearer {token}'
    json = {
        'customerName': customer_name
    }
    response = requests.patch(f'https://simple-books-api.glitch.me/orders/{order_id}', headers=headers, json=json)
    return response
