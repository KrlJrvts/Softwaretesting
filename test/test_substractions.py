from src.calculator import Calculator


def test_when_five_is_subtracted_from_six_then_one_is_returned():
    assert 6 - 5 == -1


def test_when_fifty_is_subtracted_to_twenty_then_minus_thirty_is_returned():
    assert 20 - 50 == -30
