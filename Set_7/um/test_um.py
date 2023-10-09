from um import count
import pytest


def main():
    test_um_in_str()
    test_only_um()
    test_um_in_word()


def test_um_in_str():
    assert count("Um, I like that") == 1
    assert count("I like, um, the album") == 1
    assert count("I was just, thinking, um...") == 1


def test_only_um():
    assert count("um?") == 1
    assert count("um") == 1
    assert count("....um...") == 1


def test_um_in_word():
    assert count("rump") == 0
    assert count("asumme") == 0
    assert count("I like the album") == 0

