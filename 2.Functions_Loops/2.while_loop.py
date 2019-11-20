"""
While loops
"""

is_programmer = input('Enter either Y or N: ')

while is_programmer == 'Y':
    print('Hi programmer')
else:
    print('Sorry')


i = 0

while i <= 20:
    print(f'increment # {i} ')
    i += 1
