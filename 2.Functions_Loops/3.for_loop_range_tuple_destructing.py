"""
Using for loops and the range() function
"""

my_friends = {
    'names': ['vick', 'roseline', 'pauline', 'mary', 'jane', 'gerald', 'lucy', 'derrick', 'john']
}

for names in my_friends['names']:
    print(names)

for friends in my_friends['names']:
    if friends == 'pauline':
        print(f'\n{friends} is my sister')
        continue
    if friends == 'mary':
        print(f'{friends} is my cousin \n')
        continue
    if friends == 'lucy':
        print('Exiting....\n')
        print(f'oh, and {friends} is my girl')
        break

for i in range(5):
    print(i)

for i in range(2, 4):
    print(i)

for j in range(1, 10):
    if j % 2 == 0:
        print(f'{j} is an Even number')
    elif j % 2 != 0:
        print(f'{j} is an Odd number')
