import pytest
from main import multiply


def test_multiply_decorator():
    @multiply(3)
    def return_num(num):
        return num

    assert return_num(5) == 15
    assert return_num(0) == 0
    assert return_num(-2) == -6


def test_multiply_with_float():
    @multiply(2.5)
    def return_num(num):
        return num

    assert return_num(4) == 10.0


def test_multiply_with_kwargs():
    @multiply(2)
    def add(a, b=0):
        return a + b

    assert add(3, b=4) == 14  # (3 + 4) * 2 = 14