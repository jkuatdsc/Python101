"""
Boolean operators such as ( < , > , <= , >= , == , != , and , or , not False ,not True , ) represent two states
True | False
"""

truthy = True
falsy = False

my_age = 18

user_age = int(input('Enter your age: '))

print(my_age == user_age)

"""
Combining booleans 
"""
# AND

tt = True and True
tf = True and False
ft = False and True
ff = False and False

print(f' True and True is {tt} \n', f'True and False is {tf} \n', f'False and true is {ft} \n',
      f'False and False is {ff} \n')

# OR

tt = True or True
tf = True or False
ft = False or True
ff = False or False

print(f' True or True is {tt} \n', f'True or False is {tf} \n', f'False or true is {ft} \n',
      f'False or False is {ff} \n')

# ! True

nt = not True
nf = not False
print(f' Not True is {nt} \n', f'Not False is {nf}')
