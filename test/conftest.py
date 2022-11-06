import pytest
from src.calculator import Calculator


@pytest.fixture
def calculator_object():
    return Calculator()


@pytest.fixture()
def calc(calculator_object):
    yield Calculator()  # this way we close object that we close after using (yield)
