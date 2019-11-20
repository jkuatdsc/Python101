"""
Calculating the length of lists , tuples and sets using --> | len() |
"""

my_dictionary = {
    'names': ['vick', 'alice', 'charles', 'braiden', 'darion', 'pauline', 'roseline', 'mary', 'suzie', 'kate', 'alex',
              'paul'],
    'ages': {1, 2, 3, 4, 5, 6, 7, 8, 9, 10},
    'scores': (23, 23, 3, 23, 23, 23, 23, 23, 23, 11, 43, 54, 23, 67)

}

my_list = my_dictionary['names']
my_tuple = my_dictionary['scores']
my_set = my_dictionary['ages']

list_length = len(my_list)
tuple_length = len(my_tuple)
set_length = len(my_set)

print(list_length)
print(tuple_length)
print(set_length)

# Looping through lists

for name in my_list:
    print(name)

if name in my_list == 'darion':
    print('bye!')

my_set.add(34)
print(my_set)

"""
A list [] can have repeating values while a set {} cannot have repeating values
"""

list_o = ['h', 'e', 'l', 'l', 'e', 'n']
print(list_o)

set_o = {'h', 'e', 'l', 'l', 'e', 'n'}
print(set_o)

for scores in my_tuple:
    print(scores)
    # print(f'The total of the set is {total} after adding all items in the set: ')

evens = []
odds = []
for x in range(20):
    if x % 2 == 0:
        print(f'{x} is Even:')

for x in range(20):
    if x % 2 != 0:
        print(f'{x} is Odd: ')

squares = [x ** 2 for x in range(10)]
print(f'{squares}: is a square number ')

# Matrices
matrix_one = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix_two = [
    [7, 8, 9],
    [1, 2, 3]
]

print(f'{matrix_one + matrix_two}')
print(sum(matrix_two, matrix_one))
print('name' in my_dictionary)
