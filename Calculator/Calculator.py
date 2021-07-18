from Calculator.Addition import addition
from Calculator.Subtraction import subtraction
from Calculator.Division import division
from Calculator.Multiplication import multiplication
from Calculator.Squared import squared
from Calculator.squared_root import square_root

class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def divide(self, a, b):
        self.result = round(division(a, b), 7)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def squared(self, a):
        self.result = squared(a)
        return self.result

    def Squared_root(self, a):
        self.result = square_root(a)
        return self.result

        pass