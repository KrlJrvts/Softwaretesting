import unittest
from src.calculator import Calculator


class RandomTestExamples(unittest.TestCase):
    def test_when_six_is_added_to_five_then_eleven_is_returned(self):
        # assert Calculator().add(6, 5) == 11
        expected_error = TypeError
        self.assertRaises(expected_error, Calculator.add, "six", "five")

    def test_other_assertions(self):
        self.assertEqual(Calculator().add(10, 10), 20)

    def test_assertIN(self):
        self.assertIn()
