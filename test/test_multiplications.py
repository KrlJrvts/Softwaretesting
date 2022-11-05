from src.calculator import Calculator


def test_when_five_is_multiplied_to_two_then_ten_is_returned():
    calc_multi = Calculator()
    assert calc_multi.multi(5, 2) == 10
