"""
Functions and return values
"""


def number_sum(a, b):
    """ Adds two numbers and stores the result in the variable sum """
    sum = a + b


# The number_sum function does not have a return value so it prints out None or void
# The function cannot be assigned to a variable since it doesn't have a return value so, --> is !OK, sum = my_sum(a, b)
print(number_sum(34, 2))


def number_sum_two(a, b):
    """ Adds two numbers and stores the result in the variable sum """
    sum = a + b
    return sum


# The number_sum_two function now has a return value so it prints the sum
# The function can be assigned to a variable since it has a return value so, --> is very OK, sum = my_sum(a, b)
print(number_sum_two(2, 3))
