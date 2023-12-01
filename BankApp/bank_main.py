from BankApp import bank
from BankApp.account import Account


def create_account():
    first_name = input("Enter your name")
    last_name = input("Enter your surname")
    pin = input("Enter your pin:")
    new_account = Account,bank.register()
    print("new account created successfully")
    print(new_account.str())
    goto_main_menu()


def deposit():
    account_number = input("What is your account number")
    amount = int(input("How much do you want"))
    try:
        bank.deposit(amount,account_number)
        print("deposit successfully")
    except ValueError as error:
      print(error)
    finally:
     goto_main_menu()


def withdraw():

    pass


def transfer():
    pass


def check_balance():
    pass


def goto_main_menu():
    main_menu: str = """"
    =====================================================
    Welcome to Diamond bank
    1-> Create Account
    2-> Deposit
    3-> Withdraw
    4->Transfer
    5->Check Balance
    press any key to Exist 
    ============================================================   
         """
    user_input = input(main_menu)

    def main():
        goto_main_menu()

    match user_input:
        case 1: create_account()
        case 2:deposit()
        case 3:withdraw()
        case 4:transfer()
        case 5:check_balance()


