# 1. Using input() function to get user input

my_name = input('Enter your name: ')

print(f'Hello, {my_name} ')
age = input('Enter your age: ')

# Added a new function age to convert a string into an integer

age_num = int(age)
print(f'You have lived for {age_num * 12} months {my_name}')

""" Another cleaner way to do the same calculation above """

age = int(input('Enter your age: '))
seconds = age * (60 * 60 * 24 * 365)
print(f'You have lived for {seconds} seconds {my_name}')
