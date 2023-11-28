from unittest import TestCase

from BankApp.InValidPinError import InvalidPinError
from BankApp.account import Account
from BankApp.amount_less_than_zero import AmountLessThanZero
from BankApp.invalidAmountError import InvalidAmountError


class AccountTest(unittest,TestCase):
    def setUp(self):
        self.account = Account('1', 'favour', '1234')

    def test_deposit(self):
        self.account.deposit(5000)
        self.assertEqual(5000, self.account.get_balance('1234'))
        self.account.deposit(5000)
        self.assertEqual(10000, self.account.get_balance('1234'))
        self.assertRaises(AmountLessThanZero, self.account.deposit, -5000)

    def test_get_balance_with_wrong_pin(self):
        self.account.deposit(5000)
        self.assertEqual(5000, self.account.get_balance('1234'))
        self.assertEqual(0, self.account.get_balance('1234567'))

    def test_withdrawal(self):
        self.account.deposit(5000)
        self.account.withdraw(3000, '1234')
        self.assertEqual(2000, self.account.get_balance('1234'))

    def test_withdrawal_with_wrong_pin(self):
        self.account.deposit(5000)
        self.assertRaises(InvalidPinError, self.account.withdraw, 3000, '12345')

    def test_withdraw_more_than_balance(self):
        self.account.deposit(5000)
        self.assertRaises(InvalidAmountError, self.account.withdraw, 6000, '1234')


