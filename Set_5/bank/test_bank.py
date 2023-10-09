from bank import value

def test_hello():
    assert value("Hello") == 0
    assert value("hello") == 0
    assert value("hELLo") == 0

def test_h():
    assert value("Hi there") == 20
    assert value("hi, mate") == 20
    assert value("hOW's it going?") == 20

def test_other():
    assert value ("Good morning") == 100
    assert value ("what's up?") == 100
    assert value ("Nice to see u") == 100
    assert value ("123 Hello") == 100

