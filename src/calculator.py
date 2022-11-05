class Calculator:
    def __init__(self):
        pass

    def add(self, *args):
        return sum(args)  # args allows to add n+1 arguments into

    def sub(self, first_number, second_number):
        return first_number - second_number

    def multi(self, first_number, second_number):
        return first_number * second_number

    def div(self, first_number, second_number):
        return first_number / second_number
