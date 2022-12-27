import requests


def get_books(limit='', book_type=''):
    response = requests.get(f'https://simple-books-api.glitch.me/books?type={book_type}&limit={limit}')
    return response


def get_book(book_id):
    response = requests.get(f'https://simple-books-api.glitch.me/books/{book_id}')
    return response
