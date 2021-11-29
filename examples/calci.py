import os

class Calci:
    def add(self, a, b=0):
        c = a + b
        return c

    def sub(self, a, b):
        return a - b


class StringCalci:
    def concat(self, a, b):
        return a + b

    def repeat(self, a, b):
        return a * b