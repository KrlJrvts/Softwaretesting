import pytest
from src.calculator import Calculator


@pytest.fixture
def calc():
    return Calculator()
