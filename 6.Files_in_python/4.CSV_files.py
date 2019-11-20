"""
Storing and retrieving data using CSV (Comma Separated Values) files
"""
# READING FROM THE FILE
# Ignore the first line --> strip spaces from the second line for lines in lines[1:] using a list comprehension
# Open ,read and close the file...iterate over the file contents using a for loop and use item indexes to access them
from typing import List

read_csv = open('salesdata.csv', 'r')
read_csv_contents = read_csv.readlines()
read_csv.close()

read_csv_contents = [line.strip() for line in read_csv_contents[0:]]
for lines in read_csv_contents:
    data: List[str] = lines.split(',')
    print(data)
"""
for line in read_csv_contents:
    person_data = line.split(',')  # Split the contents by a ','
    name = person_data[0].title()  # Methods from the string class to format text appearance
    age = person_data[1]
    university = person_data[2].capitalize()
    degree = person_data[3].capitalize()

    print(f'{name} is {age} years old, and studies {degree} at {university} university')
"""
# WRITING TO THE FILE

# csv_values = ','.join([Pass a list of your data separated by commas])
# ['Mary', '21', 'Cambridge', 'Business and Commerce']
for lines in read_csv_contents:
    data_to_write = lines.split(',')
    write_to_csv = ','.join(data_to_write)
    csv_file = open('csv_data.csv', 'w')
    csv_file.write(write_to_csv)
    csv_file.close()

    print(data_to_write)
