from src.calculator import Calculator
import pytest
import operator


@pytest.fixture
def calc():
    return Calculator()


def test_when_hundred_is_added_to_fifty_then_eleven_is_returned(calc):
    with pytest.raises(TypeError):
        assert calc.add(100, 50, "nine", 27) == "Boring"
