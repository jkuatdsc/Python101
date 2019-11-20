"""
Breaking down lists into smaller lists
"""

my_car_list = ['subaru forester', 'subaru imprezza', 'toyota crown', 'toyota mark x', 'vw golf', 'vw toureg']

# Slice my_car_list and assign the new list to my_car_list_two

my_car_list_two = my_car_list[0:4]
print(f'After slicing the first list: \n{my_car_list_two } \n')

# Slice my_car_list and assign the new list to my_car_list_three

my_car_list_three = my_car_list[-2:]
print(f'After slicing the first list with the last values: \n{my_car_list_three } \n')

# Printing all cars in the first list
print(f'Print all cars in the first list: \n{my_car_list[0:]} \n')

# Printing the last car in the first list
print(f'Print the last car in the first list: \n {my_car_list[-1]} \n')
