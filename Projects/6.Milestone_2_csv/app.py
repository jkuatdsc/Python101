from utils import csv

User_Choice = """
Enter:  
    - 'a' to add a new book
    - 'l' to list books
    - 'r' to mark book as read
    - 'd' to delete a book
    - 'q' to quit the application

Your choice: """


def menu():
    # csv.create_book_table()
    user_input = input(User_Choice).lower()

    while user_input != 'q':
        if user_input == 'a':
            add_new_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            mark_as_read()
        elif user_input == 'd':
            delete_book()
        else:
            print('Unknown command')
        print('')
        user_input = input(User_Choice).lower()
    print('')
    print('...Exiting the program')


def add_new_book():
    name = input('Enter the name of the book: ')
    author = input('Enter the name of the author: ')
    csv.add_book(name, author)


def list_books():
    books = csv.get_all_books()
    for book in books:
        read = 'YES' if book['read'] else 'NO'
        print(f"{book['name']} by {book['author']}, read: {read}")


def mark_as_read():
    book_to_check = input('Enter the name of the book you want to mark as read: ')
    csv.mark_as_read(book_to_check)


def delete_book():
    book_name = input('Enter the name of the book you wish to delete: ')
    csv.delete_book(book_name)


menu()
