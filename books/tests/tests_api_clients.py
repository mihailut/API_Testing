from books.requests.api_clients import *
from random import randint


class TestApiClient:

    nr = randint(1, 9999999)
    clientName = 'Wolverine'
    clientEmail = f'valid_email{nr}@email.com'
    response = login(clientName, clientEmail)

    def test_login_201_created(self):
        assert self.response.status_code == 201, 'status code is not ok'

    def test_login_409(self):
        self.response = login(self.clientName, self.clientEmail)
        assert self.response.status_code == 409, 'status code is not ok'
        assert self.response.json()['error'] == 'API client already registered. Try a different email.', 'existing user msg not ok'