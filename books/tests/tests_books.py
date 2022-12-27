from books.requests.books import get_books, get_book


class TestBooks:

    def test_get_books_200(self):
        response = get_books()
        assert response.status_code == 200, 'status code is not ok'

    def test_get_all_books(self):
        response = get_books()
        assert len(response.json()) > 0, 'total of books is wrong'

    def test_get_all_books_limit(self):
        response = get_books(limit=3)
        assert len(response.json()) == 3, 'limit is not working'

    def test_get_all_books_limit_lower_boundary(self):
        response = get_books(limit=0)
        assert len(response.json()) == 0, 'limit is not working'

    def test_get_all_books_type_fiction(self):
        response = get_books(book_type='fiction')
        assert len(response.json()) in range(1, 5), 'type fiction is not working'

    def test_get_all_books_type_non_fiction(self):
        response = get_books(book_type='non-fiction')
        assert len(response.json()) == 2, 'type non-fiction is not working'

    def test_books_invalid_type(self):
        response = get_books(book_type='abc')
        assert response.status_code == 400, 'status code is not ok'
        assert response.json()[
                   'error'] == "Invalid value for query parameter 'type'. Must be one of: fiction, non-fiction."

    def test_get_all_books_type_and_limit(self):
        response = get_books(book_type='fiction', limit=2)
        assert len(response.json()) == 2, 'type non-fiction is not working'
        assert response.json()[0]['type'] == 'fiction', 'type filter not working'
        assert response.json()[0]['id'] == 1, 'id not ok'
        assert response.json()[0]['name'] == 'The Russian', 'book name is not ok'
        assert response.json()[1]['type'] == 'fiction', 'type filter not working'
        assert response.json()[1]['id'] == 3, 'id not ok'
        assert response.json()[1]['name'] == 'The Vanishing Half', 'book name is not ok'

    def test_get_book(self):
        response = get_book(1)
        expected = {
            'author': 'James Patterson and James O. Born',
            'available': True,
            'current-stock': 12,
            'id': 1,
            'isbn': '1780899475',
            'name': 'The Russian',
            'price': 12.98,
            'type': 'fiction'}
        assert response.status_code == 200, 'status code is not ok'
        assert response.json() == expected, 'book data is not ok'

    def test_get_book_invalid_id(self):
        response = get_book(202)
        assert response.status_code == 404, 'code is not ok'
        assert response.json()['error'] == 'No book with id 202', 'invalid message is not ok'

