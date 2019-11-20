"""
There are two important keywords in loops --> Break | Continue
"""

my_cars_dict = {
    'cars': ['Subaru', 'Audi', 'Volkswagon', 'Bmw', 'Toyota', 'Mitsubishi']
}

for cars in my_cars_dict['cars']:
    if cars == 'Subaru':
        print('\n')
        print(f'Hey,{cars} Foresters are my favourite cars')
        continue
    if cars == 'Toyota':
        print(f'And, I kinda like {cars}s too')
        break  # The statement after the break keyword will not execute
    if cars == 'Mitsubishi':
        print(f'Blue {cars} are really awesome')
