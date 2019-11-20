""" A @classmethod decorator and @staticmethod decorators helps make methods more generic """


# ________________________________________________________________________________________________________________________________________________________________

# Using the @staticmethod Decorator
# ________________________________________________________________________________________________________________________________________________________________


class FixedFloat:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f'<<Fixed Float {self.amount:.2f}>>'

    @staticmethod
    def from_sum(num1, num2):
        return num1 + num2


new_float = FixedFloat.from_sum(234.54, 35.676)
print(repr(new_float))


class Ksh(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = 'Ksh.'


float_number = FixedFloat(123.768)
print(float_number)


# ________________________________________________________________________________________________________________________________________________________________

# Using the @classmethod Decorator
# ________________________________________________________________________________________________________________________________________________________________

class FixedFloatOne:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f'<<Fixed Float {self.amount:.2f}>>'

    @classmethod
    def from_sum(cls, num1, num2):  # The cls object enables the method to be called by both new_float and money
        return cls(num1 + num2)  # objects both with their respective types


new_float = FixedFloat.from_sum(234.54, 35.676)
print(repr(new_float))


class KshOne(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = 'Ksh.'

    def __repr__(self):
        return f'{self.symbol} {self.amount:.2f}'


money = KshOne(23.784)
sum_money = KshOne.from_sum(234.564, 2346.456)
print('')
print(money)
print(f'Ksh. {sum_money} ')
