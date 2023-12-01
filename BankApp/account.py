from BankApp.InValidPinError import InvalidPinError
from BankApp.amount_less_than_zero import AmountLessThanZero
from BankApp.invalidAmountError import InvalidAmountError


class Account:
    def __init__(self, account_number: str, account_name: str, pin: str):
        self.__account_number = account_number
        self.__account_name = account_name
        self.__pin = pin
        self.__balance = 0

    def deposit(self, amount: int):
        if amount > 0:
            self.__balance += amount
        else:
            raise AmountLessThanZero()

    def __validate_pin(self, pin):
        return self.__pin == pin

    def get_balance(self, pin: str):
        if self.__validate_pin(pin):
            return self.__balance
        else:
            raise InvalidPinError()

    def withdraw(self, amount: int, pin: str):
        if amount > 0:
            if self.__validate_pin(pin):
                if self.__balance >= amount:
                    self.__balance -= amount
                else:
                    raise InvalidAmountError()
            else:
                raise InvalidPinError()
        else:
            raise AmountLessThanZero()

    def get_account_number(self):
        return self.__account_number

    def get_account_name(self):
        return self.__account_name
