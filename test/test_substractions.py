from src.calculator import Calculator


def test_when_five_is_subtracted_from_six_then_one_is_returned():
    calc_sub = Calculator()
    assert calc_sub.sub(12467, 7) == 12460
