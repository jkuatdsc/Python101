"""
 Context managers
 # Opening and closing files automatically
"""
import json

with open('number_json.txt', 'r') as _numbers_file:  # Opens a file, returns a stream and closes a file.
    file_contents = json.load(_numbers_file)
print(file_contents)
