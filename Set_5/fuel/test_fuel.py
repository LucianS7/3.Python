from fuel import convert, gauge
import pytest


def test_correct_input():
    assert convert("1/2") == 50 and gauge(50) == "50%"
    assert convert("1/100") == 1 and gauge(1) == "E"
    assert convert("99/100") == 99 and gauge(99) == "F"

def test_value_error():
    with pytest.raises(ValueError):
        convert("cat/dog")

def test_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
