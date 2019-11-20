"""
lambdas --> Anonymous functions or expressions
first class, high order functions --> functions used as parameters of other functions
"""


def sum_add(a, b):
    sum_a = a + b
    return sum_a


# Using a lambda function    --> lambda x, y : (x + y)
var = lambda x, y: (x + y)

print(var(3, 5))


# Using first class functions
def who(data, identify):
    return identify(data)


def identify(some_data, age):
    return some_data['name'], age['age']


print(identify({'name': 'vick'}, {'age': 20}))
