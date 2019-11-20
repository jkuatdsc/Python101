"""
Working with integers
"""
a = 4
b = 5

sum = a + b
print(sum)

"""
Working with Strings
"""

first_name = "Victor"
last_name = "Kamau"

print(first_name + " " + last_name)

"""
Working with floating point numbers
"""
a = 20.5
b = 30.5
c = a / b

print(c)

"""
Working with boolean types
"""
t = True
print(t)

"""
Empty value or None data type
"""
x = None
print(x)

# Checking flags

a, b, c = 1, 2, 3
if any((a, b, c)):
    print('All passed')
else:
    print('Failed test')
