#!/usr/bin/env python3
import fraction
import unittest


class MyTestCase(unittest.TestCase):

    def test_plus(self):
        res = fraction.Fraction(2, 5).plus(fraction.Fraction(4, 15))
        self.assertEqual(fraction.Fraction(2, 3), res, "2/5 + 4/15 must be 2/3")
        res = fraction.Fraction(-2, 5).plus(fraction.Fraction(4, 15))
        self.assertEqual(fraction.Fraction(-2, 15), res, "-2/5 + 4/15 must be -2/15")

    def test_minus(self):
        res = fraction.Fraction(2, 5).minus(fraction.Fraction(4, 15))
        self.assertEqual(fraction.Fraction(2, 15), res, "2/5 - 4/15 must be 2/15")
        res = fraction.Fraction(-2, 5).minus(fraction.Fraction(4, 15))
        self.assertEqual(fraction.Fraction(-2, 3), res, "-2/5 - 4/15 must be -2/3")

    def test_opposite(self):
        res = fraction.Fraction(-3, 5).opposite()
        self.assertEqual(fraction.Fraction(3, 5), res, "-3/5 opposite must be 3/5")
        res = fraction.Fraction(3, 5).opposite()
        self.assertEqual(fraction.Fraction(-3, 5), res, "3/5 opposite must be -3/5")

    def test_times(self):
        res = fraction.Fraction(3, 4).times(fraction.Fraction(6, 7))
        self.assertEqual(fraction.Fraction(9, 14), res, "3/4 * 6/7 must be 9/14")
        res = fraction.Fraction(-3, 4).times(fraction.Fraction(-6, 7))
        self.assertEqual(fraction.Fraction(9, 14), res, "-3/4 * -6/7 must be 9/14")

    def test_divide_by(self):
        res = fraction.Fraction(2, 5).divide_by(fraction.Fraction(4, 15))
        self.assertEqual(fraction.Fraction(3, 2), res, "2/5 / 4/15 must be 3/2")
        res = fraction.Fraction(-2, 5).divide_by(fraction.Fraction(4, 15))
        self.assertEqual(fraction.Fraction(-3, 2), res, "-2/5 / 4/15 must be -3/2")

    def test_div_by_zero(self):
        with self.assertRaises(ZeroDivisionError, msg="division by zero must cause error"):
            fraction.Fraction(3, 4).divide_by(fraction.Fraction(0, 3))

    def test_inverse(self):
        res = fraction.Fraction(-3, 5).inverse()
        self.assertEqual(fraction.Fraction(-5, 3), res, "-3/5 inverse must be -5/3")
        res = fraction.Fraction(33, 5).inverse()
        self.assertEqual(fraction.Fraction(5, 33), res, "33/5 inverse must be 5/33")

    def test_inverse_zero(self):
        with self.assertRaises(ZeroDivisionError, msg="inversion of zero must cause error"):
            fraction.Fraction(0, 3).inverse()

    def test_parse_fraction(self):
        res = fraction.Fraction.parse_fraction("2/-4")
        self.assertEqual(fraction.Fraction(-1, 2), res, "'2/-4' must be equal to -1/2")

    def test_parse_fraction_invalid(self):
        with self.assertRaises(Exception, msg="unknown symbol must cause error"):
            fraction.Fraction.parse_fraction("2x/7")

    def test_lt(self):
        res = fraction.Fraction(2, 5) < fraction.Fraction(4, 7)
        self.assertEqual(True, res, "2/5 must be less than 4/7")
        res = fraction.Fraction(4, 7) < fraction.Fraction(2, 5)
        self.assertEqual(False, res, "2/5 must be less than 4/7")

    def test_gt(self):
        res = fraction.Fraction(2, 5) > fraction.Fraction(4, 7)
        self.assertEqual(False, res, "2/5 must be less than 4/7")
        res = fraction.Fraction(4, 7) > fraction.Fraction(2, 5)
        self.assertEqual(True, res, "2/5 must be less than 4/7")

    def test_le(self):
        res = fraction.Fraction(2, 5) <= fraction.Fraction(4, 7)
        self.assertEqual(True, res, "2/5 must be less or equal than 4/7")
        res = fraction.Fraction(2, 5) <= fraction.Fraction(2, 5)
        self.assertEqual(True, res, "2/5 must be less or equal than 2/5")

    def test_ge(self):
        res = fraction.Fraction(2, 5) >= fraction.Fraction(4, 7)
        self.assertEqual(False, res, "2/5 must be less or equal than 4/7")
        res = fraction.Fraction(4, 7) >= fraction.Fraction(4, 7)
        self.assertEqual(True, res, "4/7 must be less or equal than 4/7")

    def test_eq(self):
        res = fraction.Fraction(249, 109) == fraction.Fraction(148, 5)  # 386/3 86/113
        self.assertEqual(False, res, "249/109 ei ole 148/5")  # hash collision
        res = fraction.Fraction(2, 5) == fraction.Fraction(4, 10)
        self.assertEqual(True, res, "2/5 must be 4/10")

    def test_exact(self):
        res = fraction.Fraction(12345678901234567, 1) == \
            fraction.Fraction(12345678901234568, 1)
        self.assertEqual(False, res,
                         "12345678901234567/1 != 12345678901234568/1")

    def test_neq(self):
        res = fraction.Fraction(2, 5) != fraction.Fraction(4, 7)
        self.assertEqual(True, res, "2/5 is not 4/7")
        res = fraction.Fraction(2, 5) != fraction.Fraction(4, 10)
        self.assertEqual(False, res, "2/5 must be 4/10")


if __name__ == '__main__':
    unittest.main()

