from functools import reduce
from operator import *


class Calculator:
    def __init__(self):
        pass

    def add(self, *args):
        return reduce(add, args)  # args allows to add n+1 arguments into

    def sub(self, *args):
        return reduce(sub, args)

    def multi(self, *args):
        return reduce(mul, args)

    def div(self, *args):
        return reduce(truediv, args)
