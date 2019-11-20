class Account:
    """ A simple account class """
    """ The constructor that initializes the objects fields """

    def __init__(self, owner, amount=0.00):
        self.owner = owner
        self.amount = amount
        self.transactions = []

    def __repr__(self):
        return f'Account {self.owner},{self.amount} '

    def __str__(self):
        return f'Account belongs to {self.owner} and has a balance of {self.amount} Ksh Only '


""" Create new Accounts"""
acc1 = Account('Victor')  # Amount is initialized with a default value of 0.0
acc2 = Account('Roseline', 1000.00)  # Amount is initialized with the value 1000.00

print('')
print(str(acc2))
print(repr(acc1))
