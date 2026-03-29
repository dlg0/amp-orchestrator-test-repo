"""Tests for the calculator module."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

import pytest

from calculator import add, subtract, multiply, divide


def test_add():
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(10, 4) == 6


def test_subtract_negative():
    assert subtract(3, 7) == -4


def test_multiply_positive():
    assert multiply(3, 4) == 12


def test_multiply_negative():
    assert multiply(-2, 5) == -10


def test_multiply_zero():
    assert multiply(7, 0) == 0


def test_divide():
    assert divide(10, 2) == 5


def test_divide_float():
    assert divide(7, 2) == 3.5


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(1, 0)
