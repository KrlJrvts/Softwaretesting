from src.calculator import Calculator
import pytest


def test_when_five_is_subtracted_from_six_then_one_is_returned(calc):
    assert calc.sub(12467, 7) == 12460
