"""
 More examples on classes and objects
"""


def main():
    class Movie:
        def __init__(self, names, genre, time, rating):
            self.name = names
            self.genre = genre
            self.time = time
            self.rating = rating

        def print_movie(self):
            print('')
            movie = [
                self.name,
                self.genre,
                self.time,
                self.rating
            ]
            return movie

    movie_one = Movie('The Star', 'Animation', '12:43:43', 'Five')
    movie_two = Movie('Rango', 'Animation', '3:54:32', 'Four')

    print(movie_one.print_movie())
    print(movie_two.print_movie())


if __name__ == '__main__':
    main()
