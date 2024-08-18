import math

class operations:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return operations(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return operations(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return operations(real_part, imag_part)

    def __truediv__(self, other):
        denom = other.real ** 2 + other.imag ** 2
        real_part = (self.real * other.real + self.imag * other.imag) / denom
        imag_part = (self.imag * other.real - self.real * other.imag) / denom
        return operations(real_part, imag_part)

    def __abs__(self):
        return math.sqrt(self.real ** 2 + self.imag ** 2)

    def conjugate(self):
        return operations(self.real, -self.imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"