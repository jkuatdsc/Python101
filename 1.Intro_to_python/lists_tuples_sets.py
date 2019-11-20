"""
                                       -------------------COLLECTIONS------------------------------
Lists []
Tuples ()
Sets {} --> Store data in an unorganised way
        --> Data stored in sets cannot be accesses using indexes.
        --> The output from a set is != to the order in which data is stored on the set
"""

from _collections import *
from collections import Counter

# Deque

d = deque('a1,a2,a3')
d.append('b1')
d.popleft()

# Counter
counter = Counter()
for word in ['vick', 'vickee', 'vick', 'vick', 'john', 'paula', 'rose', 'evelyn', 'evelyn', 'paula']:
    counter[word] += 1
    print(counter)

# Lists

my_list = ['vick', 'waichigo', 'kamau']

# Tuple

my_tuple = ('rose', 'wairimu', 'kamau')

# Sets

my_set = {'paula', 'noni', 'kamau'}

"""
More operations on sets     ---> Intersection , Unions , difference etc
"""

set_one = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set_two = {5, 6, 71, 2, 3, 4, 6, 4, 55, 6, 777, 9, 42}

print(set_one.intersection(set_two))  #
print(set_one.union(set_two))
print(set_one.difference(set_two))

## Outputs

print(my_list)
print(d)
print(d[0])
print(my_tuple)
print(my_set)

print(my_list[0])
