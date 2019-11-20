"""
Using set operations to check who went to the party
"""
# Present guests using Intersection of sets
friends = {'alice', 'lucy', 'braiden', 'kim'}
guests = {'jane', 'lucy', 'paula', 'alice', 'mary'}

present = friends.intersection(guests)  # | (friends & guests)
print(present)

# Absent friends using difference of sets
absent = friends.difference(guests)
print(absent)

# Constructing a dictionary from lists

names = ['paula', 'rose', 'mary']
last_seen = [12, 3, 5]

lists_to_dict = {names[i]: last_seen[i] for i in range(len(names))}
print(lists_to_dict)

# Constructing a dictionary from lists using the function zip()
# Zip gives a list of tuples [(paula,12),(rose,3),...]
# Dict takes the list and puts it in a dictionary matching the tuples

lists_to_dict = dict(zip(names, last_seen))
print(lists_to_dict)

for key, value in lists_to_dict.items():
    print(f'{key} : {value}')
