""" name , author, read \n """

books_file = 'books.csv'


def create_book_table():
    with open(books_file, 'w'):
        pass


def add_book(name, author):
    with open(books_file, 'a') as csv_file:
        csv_file.write(f'{name}, {author}, 0 \n')


def get_all_books():
    with open(books_file, 'r') as csv_file:
        lines = [lines.strip().split(',') for lines in csv_file.readlines()]
        return [
            {'name': line[0], 'author': line[1], 'read': line[2]}
            for line in lines
        ]


def mark_as_read(name):
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = '1'
    _save_all_books(books)


def _save_all_books(books):
    with open(books_file, 'w') as csv_file:
        for book in books:
            csv_file.write(f"{book['name']}, {book['author']}, {book['read']} \n")


def delete_book(name):
    books = get_all_books()
    for book in books:
        if book['name'] != name:
            _save_all_books(books)


if __name__ == '__main__':
    print('This module works. ')
