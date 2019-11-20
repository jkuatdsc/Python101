"""
 #Using json (javascript object notation)
    -->json is a string
    -->must use double quotation marks
    -->the outermost structure should be an object
    -->import the json module
"""
import json
import timeit

# Open the friends_json.txt file
file_open = open('friends_json.txt', 'r')
file_contents = json.load(file_open)

file_open.close()

print(file_contents)
print(file_contents['friends'][0])

# Writing to a json file
# Save a list of cars as a json object

cars = [
    {'make': 'Toyota', 'model': 'Allion'},
    {'make': 'Toyota', 'model': 'Crown'},
    {'make': 'Toyota', 'model': 'Mark x'},
    {'make': 'Subaru', 'model': 'Imprezza'},
    {'make': 'Subaru', 'model': 'Forester'},
    {'make': 'Subaru', 'model': 'Legacy'},
    {'make': 'Volkswagen', 'model': 'Toureg'},
    {'make': 'Volkswagen', 'model': 'Tiguan'},
    {'make': 'Volkswagen', 'model': 'Golf'},
    {'make': 'Volkswagen', 'model': 'Beetle'}
]
# Open the file to write to
open_cars_file = open('cars_json.txt', 'w')
# Use json.dump(data, file_pointer) to write contents | use json pretty printing to format the output
json.dump(cars, open_cars_file, sort_keys=True, indent=4)
open_cars_file.close()

print(timeit.timeit())
