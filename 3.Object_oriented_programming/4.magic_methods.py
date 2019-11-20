""" Dunder methods is a fancy name for 'under under method under under' or __method__()
They are built-in functions that add functionality to python code and also unlock new features on objects """


class Garage:
    """ Stores cars in a garage object """

    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, car):
        return self.cars[car]

    def __repr__(self):
        return f'--> {self.cars}'

    def __str__(self):
        return f'--> {self.cars}'


Toyota = Garage()
print(Toyota.cars)

Toyota.cars.append('Mark X')
Toyota.cars.append('Allion')
Toyota.cars.append('Crown')
Toyota.cars.append('Prado')
Toyota.cars.append('Noah')

print(Toyota.cars)
print(len(Toyota))  # Its now possible to check the # of cars in the garage because of the __len__() dunder method

print(Toyota[0])  # Use the __getitem__() dunder method to enable indexing of cars in the garage

print('')
# These two methods also unlock a new functionality on the garage, iterating over cars in the garage
for cars in Toyota:
    print(f'--> {cars}')

print('')
print(repr(Toyota.cars))  # Using __repr__() to print out cars in the garage
print(str(Toyota.cars))  # Using __str__() to print out cars in the garage
