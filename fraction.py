#!/usr/bin/env python3
"""
 fraction.py - fraction as pair of integers
"""


class Fraction(object):
    
    __numerator = 0
    __denominator = 1

    @staticmethod
    def gcd(a, b):
        m = int(max(abs(a), abs(b)))
        n = int(min(abs(a), abs(b)))
        if n == 0:
            raise ArithmeticError("zero not allowed in gcd")
        while n > 0:
            mod = m % n
            m = n
            n = mod
        return m

    def __init__(self, numerator, denominator):
        numer = int(numerator)
        denom = int(denominator)
        if denom == 0:
            raise ZeroDivisionError("denominator cannot be zero")
        if numer == 0:
            denom = 1
        else:
            greatest_common_divisor = Fraction.gcd(numer, denom)
            numer = numer // greatest_common_divisor
            denom = denom // greatest_common_divisor
        if denom < 0:
            numer = -numer
            denom = -denom
        self.__numerator = numer
        self.__denominator = denom

    def numerator(self):
        return self.__numerator

    def denominator(self):
        return self.__denominator

    def real_value(self):
        return self.numerator()/self.denominator()

    def __str__(self):
        return str(self.numerator()) + "/" + str(self.denominator())

    def __repr__(self):
        return "Fraction(" + str(self.numerator()) + ", " + str(self.denominator()) + ")"

    def __eq__(self, other):
        # return self.real_value() == other.real_value()
        # return self.__hash__() == other.__hash__()
        return self.numerator()*other.denominator() == self.denominator()*other.numerator()

    def __gt__(self, other):
        return self.numerator()*other.denominator() > self.denominator()*other.numerator()

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    def __bool__(self):
        return self.numerator() != 0

    def __hash__(self):
        return hash(str(self))   # % 2147483648  # to make it 32-bit

    def plus(self, other):
        return Fraction(self.numerator()*other.denominator() +
                    self.denominator()*other.numerator(),
                    self.denominator()*other.denominator())

    def opposite(self):
        return Fraction(-self.numerator(), self.denominator())

    def inverse(self):
        return Fraction(self.denominator(), self.numerator())

    def minus(self, other):
        return self.plus(other.opposite())

    def times(self, other):
        return Fraction(self.numerator()*other.numerator(),
                    self.denominator()*other.denominator())

    def divide_by(self, other):
        return self.times(other.inverse())

    @staticmethod
    def parse_fraction(tekst):
        numer, denom = tekst.split("/")
        return Fraction(numer, denom)


def main():
    """
    Main method.
    """
    m1 = Fraction(2, 5)      # 2/5
    m2 = Fraction(4, 15)     # 4/15
    print(m1.plus(m2))       # 2/5 + 4/15 = 2/3
    m3 = Fraction(0, 1)      # 0/1
    print(m1.times(m3))
    print(m1.divide_by(m3))


if __name__ == '__main__':
    main()
