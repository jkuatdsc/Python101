"""
A simple app to add, list, search, mark books as read and delete books on a json file
"""
import json

books = "books.json"


def add_book(author, title):
    global books
    books = list_books()
    books.append({'author': author, 'title': title, 'read': False, '': '\n'})
    _save_all_books_(books)


def list_books():
    with open('books.json', 'r') as json_file:
        return json.load(json_file)


def search_book(name):
    global books
    books = list_books()
    for book in books:
        if book['title'] == name:
            return book


def mark_as_read(name):
    global books
    books = list_books()
    for book in books:
        if book['title'] == name:
            book['read'] = True
    _save_all_books_(books)


def _save_all_books_(books):
    with open('books.json', 'w') as json_file:
        json.dump(books, json_file, sort_keys=True, indent=4)


def delete_book(name):
    global books
    books = list_books()
    books = [book for book in books if book['title'] != name]
    _save_all_books_(books)


if __name__ == '__main__':
    print('All functions are go')
