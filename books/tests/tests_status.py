from books.requests.status import *


class TestStatus:

    def test_status_200(self):
        assert get_status().status_code == 200, 'Status code is not corect'
        assert get_status().json()['status'] == 'OK', 'Status message is incorrect'