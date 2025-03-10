# test_main.py

import pytest
from main import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 3) == -3

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 3) == -3

def test_divide():
    assert divide(6, 3) == 2
    assert divide(5, 2) == 2.5

    with pytest.raises(ValueError):
        divide(5, 0)
