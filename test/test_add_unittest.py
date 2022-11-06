import unittest
from src.calculator import Calculator


class RandomTestExamples(unittest.TestCase):
    def test_when_six_is_added_to_five_then_eleven_is_returned(self):
        # assert Calculator().add(6, 5) == 11
        self.assert_(Calculator().add(6, 5), 11)
