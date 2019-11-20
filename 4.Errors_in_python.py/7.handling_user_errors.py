"""
 # Handling user errors
"""


def square():
    user_input = input('Enter a number: ')
    number = 0
    try:
        number = float(user_input)
    except ValueError:
        if user_input == '':
            user_input = 'null'
        print(f'The value {user_input} is NaN')
    else:
        print('The code now works')
    finally:
        number_squared = number ** 2
    return number_squared


print(square())


# OR

def square_two():
    user_input = input('Enter a number: ')
    try:
        n = 0
        n = float(user_input)
        n_squared = n ** 2
        return n_squared
    except ValueError:
        if user_input == '':
            user_input = 'null'
        print(f'The value {user_input} is NaN')
        return 0


print(square_two())
