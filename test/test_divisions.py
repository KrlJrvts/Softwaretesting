import pytest
from src.calculator import Calculator


@pytest.fixture
def calc():
    return Calculator()


def test_when_ten_is_divided_to_five_then_two_is_returned(calc):
    assert calc.div(10, 5) == 2


def test_when_ten_is_divided_by_ten_then_five_is_returned(calc):
    with pytest.raises(TypeError):
        calc.div("Chicken", "egg")


def test_when_minus_hundred_is_divided_to_five_then_minus_twenty_is_returned(calc):
    assert calc.div(-100, 5) == -20


def test_when_hundred_is_divided_to_zero_then_minus_twenty_is_returned(calc):
    with pytest.raises(ZeroDivisionError):
        calc.div(100, 0)


def test_when_hundred_is_divided_to_100_then_one_is_returned(calc):
    assert calc.div(100, 100) == 1
