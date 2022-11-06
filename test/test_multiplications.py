from src.calculator import Calculator
import pytest


def test_when_five_is_multiplied_to_two_then_ten_is_returned(calc):
    assert calc.multi(5, 2) == 10
