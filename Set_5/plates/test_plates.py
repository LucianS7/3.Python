from plates import is_valid
import pytest

def test_start_with_two_letters():
    assert is_valid("CS") == True
    assert is_valid("50CS") == False
    assert is_valid("C501") == False
    assert is_valid("5CS11") == False

def test_min_and_max_caracters():
    assert is_valid("CS50") == True
    assert is_valid("CS") == True
    assert is_valid("C") == False
    assert is_valid("CS500000") == False

def test_numbers_end_of_plates():
    assert is_valid("CS50") == True
    assert is_valid("CS50A") == False

def test_numbers_dont_start_with_zero():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False

def test_punctuation():
    assert is_valid("CS!50") == False
    assert is_valid("CS,50") == False
    assert is_valid("CS 50") == False

