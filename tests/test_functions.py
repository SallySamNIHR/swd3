from hypot.functions import addition, squared, square_root, hypot
import pytest


# test addition
def test_add_int():
    assert addition(4, 7) == 11


def test_add_float():
    assert addition(1.1, 5.78) == pytest.approx(6.88, 0.0000001)


def test_add_str():
    assert addition("a", "b") == "Please enter int or float"


# test squared
def test_sqr_odd():
    assert squared(3) == 9


def test_sqr_even():
    assert squared(6) == 36


# test square root
def test_sqrt_pos():
    assert square_root(100) == 10


# test hypot
def test_hypot():
    assert hypot(3, 4) == 5
