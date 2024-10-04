import unittest
from calculator import addition, subtraction, multiplication, division


class TestSimpleCalculator(unittest.TestCase):

    def test_addition(self):
        # Test cases for addition
        self.assertEqual(addition([2, 3]), 5)
        self.assertEqual(addition([10, 5.5]), 15.5)
        self.assertEqual(addition([-1, 2]), 1)
        self.assertEqual(addition([0, 0]), 0)
        self.assertEqual(addition([1.23456, 2.34567]), 3.58023)  # rounding to 5 decimal places

    def test_subtraction(self):
        # Test cases for subtraction
        self.assertEqual(subtraction([10, 5]), 5)
        self.assertEqual(subtraction([5.5, 2.5]), 3)
        self.assertEqual(subtraction([-1, 1]), -2)
        self.assertEqual(subtraction([0, 0]), 0)
        self.assertEqual(subtraction([5.12345, 1.12345]), 4.00000)

    def test_multiplication(self):
        # Test cases for multiplication
        self.assertEqual(multiplication([2, 3]), 6)
        self.assertEqual(multiplication([1.5, 2]), 3)
        self.assertEqual(multiplication([0, 5]), 0)
        self.assertEqual(multiplication([-2, 3]), -6)
        self.assertEqual(multiplication([1.23456, 2.34567]), 2.89606)  # rounding to 5 decimal places

    def test_division(self):
        # Test cases for division
        self.assertEqual(division([6, 3]), 2)
        self.assertEqual(division([5.5, 2.2]), 2.5)
        self.assertEqual(division([0, 1]), 0)
        self.assertEqual(division([10, 5]), 2)
        self.assertEqual(division([1.23456, 2]), 0.61728)  # rounding to 5 decimal places

        # Test division by zero
        self.assertEqual(division([5, 0]), "div by zero error")
        self.assertEqual(division([10, 2, 0]), "div by zero error")


if __name__ == '__main__':
    unittest.main()
