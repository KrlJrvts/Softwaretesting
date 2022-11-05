from src.calculator import Calculator


def test_when_ten_is_divided_to_five_then_two_is_returned():
    calc_div = Calculator()
    assert calc_div.div(10, 5) == 2
