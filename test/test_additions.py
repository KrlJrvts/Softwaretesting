from src.calculator import Calculator
import pytest


def test_when_hundred_is_added_to_fifty_then_eleven_is_returned():
    calc_add = Calculator()
    with pytest.raises(TypeError):
        assert calc_add.add(100, 50, "nine", 27) == "Boring"
