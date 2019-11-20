"""
Get friends from the user, check the friends, copy them to nearby friends
"""

get_friends = input('Enter friends separated by a comma: ').split(',')
friends_set = set(get_friends)

people_list = open('people.txt', 'r')
people_list_contents = [line.strip() for line in people_list.readlines()]  # Use a list comprehension to remove the \n's
people_list.close()

people_list_set = set(people_list_contents)
nearby_people = friends_set.intersection(people_list_set)

write_nearby_people = open('nearby.txt', 'w')
friends: str

for friends in nearby_people:
    write_nearby_people.write(f'{friends} \n')
write_nearby_people.close()

# tanya,vick,alice,mary,darion,abigael,faith,ashley,hannah,keith,emma,pauline,jane,christian,mike,roseline,rose,tifanny,sophie
