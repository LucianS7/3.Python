from working import convert
import pytest

def main():
    test_time()
    test_format()
    test_hour()
    test_minute()


def test_time():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("11:15 AM to 6:25 PM") == "11:15 to 18:25"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"

def test_format():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
        convert("10 PM tot 6 PM")

def test_hour():
    with pytest.raises(ValueError):
        convert("14:22 AM to 5:22 PM")
        convert("10:22 AM to 15:22 PM")

def test_minute():
    with pytest.raises(ValueError):
        convert("10:60 AM to 5:22 PM")
        convert("10:22 AM to 5:64 PM")

if __name__ == "__main__":
    main()