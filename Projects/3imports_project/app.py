"""
Access the imported module with app.py
-->import module = import module_name
-->import a function in the module = from module_name import function_name
-->import everything in a module = from module_name import *
-->Create a new name for the module or func using --> 'as' new_name
-->You can import two or more functions or variables separated by commas
"""
from .file_operations import read_from_file, name
from .file_operations import save_to_file as save_tf

save_tf('\nThis is just a simple module', 'data.txt')

data = read_from_file('data.txt')
print(name)
print(data)
