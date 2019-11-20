"""
A simple module to demonstrate content managers
"""
print('Module imported with 0 errors.')
name = 'loading module data....'


def save_to_file(content, filename):
    with open(filename, 'w') as file:
        file.write(content)


def read_from_file(filename):
    with open(filename, 'r') as file:
        return file.read()
