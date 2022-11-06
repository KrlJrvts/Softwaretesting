from functools import reduce
from operator import *


class Calculator:
    def __init__(self):
        self.current_value = 0

    def add(self, *args):
        self.current_value = self.current_value + sum(args)
        return reduce(add, args)  # args allows to add n+1 arguments into

    def sub(self, *args):
        for number in args:
            self.current_value = self.current_value - number
        return reduce(sub, args)

    def multi(self, *args):
        return reduce(mul, args)

    def div(self, *args):
        return reduce(truediv, args)
