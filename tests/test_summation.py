import pytest
from summation import summation


def test_identity():
    assert summation(5, lambda x: x) == 15


def test_squares():
    assert summation(5, lambda x: x * x) == 55


def test_cubes():
    assert summation(3, lambda x: x ** 3) == 36


def test_one():
    assert summation(1, lambda x: x) == 1


def test_constant():
    assert summation(4, lambda x: 1) == 4


def test_large():
    assert summation(100, lambda x: x) == 5050
