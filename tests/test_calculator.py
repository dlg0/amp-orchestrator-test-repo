"""Tests for the calculator module."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from calculator import add, subtract, multiply


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
