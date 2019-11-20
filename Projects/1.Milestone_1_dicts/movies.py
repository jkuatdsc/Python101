"""
This is a simple movie storage application implemented using collections
"""

movies = []  # {'name' ,'director' , 'year', 'genre' ,'rating'}


def menu():
    user_input = input('Enter A to add a movie:,F to find a movie: , L to list movies:,D to delete a movie: Q to quit '
                       'the application :: --> ').lower()

    while user_input != 'q':
        if user_input == 'a':
            addmovie()
        elif user_input == 'f':
            findmovie()
        elif user_input == 'l':
            listmovie(movies)
        elif user_input == 'd':
            deletemovie()
        else:
            print('Unknown command, Try again')
        print('')
        user_input = input(
            '\nEnter A to add a movie:,F to find a movie: , L to list movies:,D to delete a movie: Q to quit '
            'the application :: --> ').lower()
    print('')
    print('...Exiting the program...Adios!')


def addmovie():
    name = input('Enter the name of the movie: ')
    director = input('Enter the director\'s name: ')
    year = input('Enter the year: ')
    genre = input('Enter the movie\'s genre: ')
    rating = input('Enter the movie\'s rating: ')

    movies.append({
        'name': name,
        'director': director,
        'year': year,
        'genre': genre,
        'rating': rating
    })


def listmovie(movie_list):
    for movie in movies:
        list_movie_details(movie_list)


def list_movie_details(movielist):
    print(movies)


def findmovie(name):
    find_by = input('What property are you looking for?, eg Year,director etc :')
    looking_for = input('What are you looking for? :')

    found_movies = find_by_attribute(movies, looking_for, lambda x: x[find_by])

    listmovie(found_movies)
    return name


def find_by_attribute(items, expected, finder):
    found = []

    for i in items:
        if finder(i) == expected:
            found.append(i)
    return found


def deletemovie():
    name = input('Enter the movie to delete: ')
    mdel = list(movies)
    for i in mdel:
        if mdel[0] == name:
            mdel.remove(1)


menu()
