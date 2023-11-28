import unittest

from BankApp.bank import Bank


class BankTest(unittest.TestCase):
    def setUp(self):
        self.bank = Bank('FCMB')
        self.bank.register('Dera', 'Delight', '1234')

    def test_register(self):
        self.bank.register('Dera', 'Delight', '1234')
        self.assertEqual('Dera Delight', self.bank.get_account('2337167900').get_account_name())

    def test_deposit_and_check_balance(self):
        self.bank.deposit(6000, '2337167900')
        self.assertEqual(6000, self.bank.check_balance('2337167900', '1234'))

    def test_withdrawal(self):
        self.bank.deposit(6000, '2337167900')
        self.assertEqual(6000, self.bank.check_balance('2337167900', '1234'))
        self.bank.withdraw(5000, '2337167900', '1234')
        self.assertEqual(1000, self.bank.check_balance('2337167900', '1234'))

    def test_transfer(self):
        self.assertEqual('Dera Delight', self.bank.get_account('1').get_account_name())
        self.bank.deposit(10000, '1')
        self.assertEqual(10000, self.bank.check_balance('1', '1234'))
        self.bank.register('Dera', 'Delight', '4321')
        self.assertEqual('Dera Delight', self.bank.get_account('2').get_account_name())
        self.assertEqual(0, self.bank.check_balance('2', '4321'))
        self.bank.transfer(5000, '1', '2', '1234')
        self.assertEqual(5000, self.bank.check_balance('1', '1234'))
        self.assertEqual(5000, self.bank.check_balance('2', '4321'))
