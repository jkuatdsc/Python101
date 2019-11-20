""" Store and retrieve data from a list """
from typing import List, Any

books: List[Any] = []


def add_book(name, author):
    books.append({'name': name, 'author': author, 'read': False})


def get_all_books():
    return books


def mark_as_read(name):
    for book in books:
        if book['name'] == name:
            book['read'] = True


def delete_book(name):
    global books
    books = [book for book in books if book['name'] != name]
