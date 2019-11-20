import math

"""
Declaring|prototyping , defining|implementing  and calling|invoking functions
# def area(n,f):   --> n and f are called |parameters|
# area(3,4)        --> 3 and 4 are called |arguments|
"""
# Simple greet function
my_name = 'Vick'


def say_hello():
    print(f'Hi there {my_name}')


say_hello()


# A simple function to calculate the volume of a sphere


def sphere_volume(r):
    """ A function that calculates the volume of a sphere """
    volume = (4.0 / 3.0) * math.pi * r ** 3
    return volume


if __name__ == '__main__':
    import timeit

    print(f'The running time of the sphere_volume function is : {timeit.timeit("sphere_volume(14)",
                                                                               setup="from __main__ import sphere_volume")}')



vol = sphere_volume(6)
print(vol)


# A simple function to calculate the area of rectangles and squares


def area(l, w):
    """ Calculates the area using the length and width of squares and rectangles """
    area = (l * w)
    return area


area_rect = area(2, 3)
area_square = area(3, 5)

print(f'The area of the rectangle is: {area_rect}')
print(f'The area of the square is: {area_square}')


# A simple function to print out even and odd numbers

def even_and_odd(n):
    """ A function that returns all even and odd numbers between a range n"""
    for num in range(n):
        if num % 2 == 0:
            print(f'{num} is an Even number')
        elif num % 2 != 0:
            print(f'{num} is an Odd number')
    return n


numbers = even_and_odd(10)
print(numbers)
