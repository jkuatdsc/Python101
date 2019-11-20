## Printing and formatting Strings

print("Hello Victor")
print('Hello Victor')

# Printing Quotes ("",'')
print("Hey there,it's me ")
print('He said, "You are amazing" ')

# Using escaped quotes
print("He said, \"You are amazing\" ")

# ---------------------------------------------------------------------#

name = 'Victor'
print('Hello ' + name)

name = 'John'
print('Hello ' + name)

# Using f string (Formatted Strings)
name = 'Paula'
greeting = f'Hello, {name}'
print(greeting)

another_greeting = 'Hi, {}'
Formatted_greeting = another_greeting.format(name)
print(Formatted_greeting)
