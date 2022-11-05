from src.calculator import Calculator


def test_when_hundred_is_added_to_fifty_then_eleven_is_returned():
    calc_add = Calculator()
    assert calc_add.adding(100, 50) == 150
