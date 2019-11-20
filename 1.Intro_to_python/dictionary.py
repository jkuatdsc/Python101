"""
Using dictionaries
"""

dictionary_one = {
    'number': 20,
    'string': "kamau",
    'double': 23.5
}
my_combined_dict = {

}

# Using dictionaries with lists , tuples and sets

my_dictionary = {
    'friend': ['vick', 'sylvie', 'moses', 'albert', 'price', 'keith'],
    'speciality': {'android_dev', 'machine_learning', 'web_dev', 'game_dev'},
    'age': (12, 75, 15, 35, 14)
}
for key, value in enumerate(my_dictionary):
    print(f'{key} = {value}')

# Adding items in lists, tuple or sets

test_add = my_dictionary['age']
print(sorted(test_add))
print()
print(sum(test_add))

# Combining lists , dictionaries , sets  and tuples  & adding a new dictionary to my_variable

my_variable = [
    {
        'name': ('victor', 'waichigo', 'kamau'),
        'age': 20,
        'hobbies': ['coding', 'travelling', 'reading', 'bike_riding']
    },  # The comma separates the dictionaries just like it does to list items
    {
        'name': ('paula', 'noni', 'kamau'),
        'age': 18,
        'hobbies': {'swimming', 'travelling', 'hiking'}
    }
]

# Items in a dictionary are accesed using the key value unlike lists which use indexes []

varone = my_variable[0]  # Accesing items in the list
vartwo = my_variable[1]

print(varone['name'])
print(varone['age'])
print(varone['hobbies'])

print('\n')

print(vartwo['name'])
print(vartwo['age'])
print(vartwo['hobbies'])
