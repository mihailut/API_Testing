import requests
from random import randint


def login(client_name=None, client_email=None):
    json = {
        "clientName": client_name,
        "clientEmail": client_email
    }
    response = requests.post('https://simple-books-api.glitch.me/api-clients/', json=json)
    return response
    # in spate la login se trimtie un json
    # aici ne definim jsonul pe care vrem sa il trimitem


def get_token():
    nr = randint(1, 99999)
    json = {
        "clientName": 'Gicu',
        "clientEmail": f'valid_email{nr}@gmail.com'
    }
    response = requests.post('https://simple-books-api.glitch.me/api-clients/', json=json)
    return response.json()['accessToken']


def invalid_login(client_name=None):
    invalid_json = {
        'clientName': client_name,
    }
    response = requests.post('https://simple-books-api.glitch.me/api-clients/', json=invalid_json)
    return response
