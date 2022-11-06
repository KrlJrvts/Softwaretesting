import unittest
from src.calculator import Calculator


class RandomTestExamples(unittest.TestCase):

    """
        def test_when_six_is_added_to_five_then_eleven_is_returned(self):
            # assert Calculator().add(6, 5) == 11
            expected_error = TypeError
            self.assertRaises(expected_error, Calculator.add, "six", "five")

        def test_other_assertions(self):
            self.assertEqual(Calculator().add(10, 10), 20)
    """

    def test_assertEqual(self):
        self.assertEqual(Calculator().div(10, 5), 2)

    def test_assertIsEqual(self):
        self.assertNotEqual(Calculator().div(10, 5), 3)

    def test_assertIsNotNone(self):
        self.assertIsNotNone(Calculator.div(10, 5))

    def test_assertNotEqual(self):
        self.assertNotEqual(Calculator.div(10, 5), 3)

    def test_assert_expected_error(self):
        expected_error = TypeError
        values = Calculator().div
        self.assertRaises(expected_error, values, "Ten", "Five")


#
