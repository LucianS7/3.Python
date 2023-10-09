from numb3rs import validate

def main():
    test_format()
    test_range()

def test_format():
    assert validate("1.1.1.1") == True
    assert validate("1.1.1") == False
    assert validate("1.1.") == False
    assert validate("1") == False

def test_range():
    assert validate("127.2.1.1") == True
    assert validate("127.275.1.1") == False
    assert validate("127.1.275.1") == False
    assert validate("127.1.1.275") == False
    assert validate("127.1.1.0") == True

if __name__ == "__main__":
    main()