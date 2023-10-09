import pytest
from unittest.mock import Mock
from unittest.mock import MagicMock
from jar import Jar

def main():
    test_init()
    test_deposit()
    test_withdraw_without_mock()
    test_withdraw_with_mock()
    test_str()


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    jar.deposit(5)
    assert jar.size == 10
    with pytest.raises(ValueError):
        jar.deposit(3)


def test_withdraw_without_mock():
     jar = Jar()
     jar.deposit(12)
     jar.withdraw(2)
     assert jar.size == 10
     jar.withdraw(5)
     with pytest.raises(ValueError):
         jar.withdraw(7)


def test_withdraw_with_mock():
    jar_mock = Mock(spec=Jar)
    jar_mock.size = 10
    jar_mock.withdraw.side_effect = lambda n: setattr(jar_mock, 'size', jar_mock.size - n)
    jar_mock.withdraw(5)
    jar_mock.withdraw.assert_called_once_with(5)
    assert jar_mock.size == 5


def test_withdraw_with_magicmock():
    jar = Jar()
    jar.withdraw = MagicMock()
    jar.withdraw(5)
    jar.withdraw.assert_called_with(5)


def test_str():
    jar = Jar()
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"
    jar.deposit(4)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪"


if __name__ == "__main__":
    main()