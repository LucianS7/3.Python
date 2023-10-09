import pytest
from unittest import TestCase
from unittest.mock import patch
from jar import Jar

class JarWithdrawTestCase(TestCase):
    @patch.object(Jar, '_size', 5)
    def test_withdraw(self, mock_size):
        jar = Jar()
        jar.deposit(10)
        jar.withdraw(3)
        self.assertEqual(jar.size, 2)

    def test_withdraw_not_enough_cookies(self):
        jar = Jar()
        jar.deposit(5)
        with self.assertRaises(ValueError):
            jar.withdraw(10)