""" The controller module for that handles user interaction"""
from utils import json_storage

User_Choice = """
Enter:  
    - 'a' to add a new book
    - 'l' to list books
    - 's' to search for a book
    - 'r' to mark book as read
    - 'd' to delete a book
    - 'q' to quit the application

Your choice: """


def menu():
    user_input = input(User_Choice)

    while user_input != 'q':
        if user_input == 'a':
            add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 's':
            search_book()
        elif user_input == 'r':
            mark_book_as_read()
        elif user_input == 'd':
            delete_book()
        else:
            print('')
            print("Unknown Command, Please try again! ")
        user_input = input(User_Choice)
    print('')
    print('Exiting the program....Adios')


def add_book():
    name = input('Enter the Authors name: ')
    title = input('Enter the book title: ')

    json_storage.add_book(name, title)
    print(json_storage.add_book(name, title))


def list_books():
    json_storage.list_books()
    print('')
    for books in json_storage.list_books():
        print(books)


def search_book():
    name_to_search = input('Enter name to search: ')

    json_storage.search_book(name_to_search)
    print(json_storage.search_book(name_to_search))


def mark_book_as_read():
    book_to_mark = input('Enter the book to mark as read: ')

    json_storage.mark_as_read(book_to_mark)
    print(json_storage.mark_as_read(book_to_mark))


def delete_book():
    book_to_delete = input('Enter the book to delete: ')

    json_storage.delete_book(book_to_delete)


if __name__ == '__main__':
    menu()
