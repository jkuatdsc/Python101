"""
use list (expression)
"""
# Numbers

my_num_list = list(range(10))
print(my_num_list)

my_doubled_list = list(n * 2 for n in my_num_list)
print(my_doubled_list)

my_tripled_list = list(n * 3 for n in my_num_list)
print(my_tripled_list)

# Strings

phrases = [f'I am {age} years old' for age in my_tripled_list]
print(phrases)

# Convert to lowercase
name_list = ['vick', 'Roseline', 'Pauline', 'lucy']
lowercase_name = [names.lower() for names in name_list]
print(lowercase_name)

# Convert to uppercase
uppecase_names = [names.upper() for names in name_list]
print(uppecase_names)

# Convert first letter to uppercase
first_letter_uppercase = [names.capitalize() for names in name_list]
print(first_letter_uppercase)

# Party attendance
friends = ['alice', 'lucy', 'braiden', 'kim']
guests = ['jane', 'lucy', 'paula', 'alice', 'mary']

present = [name for name in friends if name in guests]
print(f'\n {present[0]} and {present[1]} attended the party')
