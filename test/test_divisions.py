import pytest

from src.calculator import Calculator


def test_when_ten_is_divided_to_five_then_two_is_returned():
    calc_div = Calculator()
    assert calc_div.div(10, 5) == 2


def test_when_ten_is_divided_by_teo_then_five_is_returned():
    calc_div_2 = Calculator()
    with pytest.raises(TypeError):
        calc_div_2.div("Chicken", "egg")


def test_when_minus_hundred_is_divided_to_five_then_minus_twenty_is_returned():
    calc_div_3 = Calculator()
    assert calc_div_3.div(-100, 5) == -20


def test_when_hundred_is_divided_to_zero_then_minus_twenty_is_returned():
    calc_div_4 = Calculator()
    with pytest.raises(ZeroDivisionError):
        calc_div_4.div(100, 0)


def test_when_hundred_is_divided_to_100_then_one_is_returned():
    calc_div_3 = Calculator()
    assert calc_div_3.div(100, 100) == 1

def test_float_
