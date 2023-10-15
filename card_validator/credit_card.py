# import re
#
# card_type = " "
# card_number = " "
# validity_status = " "
#
#
# def card_validity():
#     if 13 <= len(card_number) <= 16:
#         return True
#     return False
#
#
# def card_type_validator(card_number: str):
#     if card_validity():
#         global card_type
#         if card_number.startswith("4"):
#             card_type += "Visa"
#         elif card_number.startswith("5"):
#             card_type += "Master Card"
#         elif card_number.startswith("37"):
#             card_type += "American Express Cards"
#         elif card_number.startswith("6"):
#             card_type += "Discover Card"
#         else:
#             card_type += "Invalid"
#     return card_type
#
#
# def card_type_validator(card_number: str):
#     global validity_status
#     validity_status = "Invalid"
#     if card_validity():
#         even_Total = 0
#         odd_Total = 0
#     for count in range(len(card_number)):
#         if count % 2 == 0:
#             digit = int(card_number[count])
#             new_digit = digit * 2
#             if new_digit >= 10: even_Total += ((new_digit % 10) + (new_digit // 10))
#         else:
#             even_Total += new_digit
#
#         if count % 2 != 0:
#             digit = int(card_number[count])
#             odd_Total += digit
#     total_digits = even_Total + odd_Total
#     if total_digits % 10 == 0:
#         validity_status = "Valid"
#     else:
#         validity_status = "Invalid"
#     return validity_status
#
#
# def input_():
#     global card_number
#
#     user_card_number = input("Hello,enter card details: ")
#     if re.search("^[0 +9] + $", user_card_number):
#         if 13 <= len(user_card_number) <= 16:
#             card_number = user_card_number
#             card_type_validator(user_card_number)
#             card_validity(user_card_number)
#             print()
#             print("*" * 40,
#                   "\n**Credit Card Type: ", card_type,
#                   "\n**Credit Card Number: ", user_card_number,
#                   "\n**Credit Card Digit Length: ", len(user_card_number),
#                   "\n**Credit Card Validity Status:", validity_status,
#                   "\n", "*" * 40)
#         else:
#             print("Credit Card number must be between 13 and 16")
#             input_()
#     else:
#         print("Credit Card must not be blank \nTry Again")
#         input_()
#
# 
# if __name__ == '__main__':
#     input_()


import re

type = ""
card_number = ""
validity_status = ""


def is_card_valid():
    if 13 <= len(card_number) <= 16:
        return True
    return False


def card_type_detector(card_number: str):
    if is_card_valid():
        global type
        if card_number.startswith("4"):
            type += "Visa"
        elif card_number.startswith("5"):
            type += "MasterCard"
        elif card_number.startswith("37"):
            type += "America ExpressCard"
        elif card_number.startswith("6"):
            type += "Discover Card"
        else:
            type += "Invalid Card"

    else:
        type += "Invalid Card"

    return type


def card_validity_detector(card_number: str):
    global validity_status
    validity_status = "Invalid"

    if is_card_valid():
        even_total = 0
        odd_total = 0

        for counter in range(len(card_number)):

            if counter % 2 == 0:
                digit = int(card_number[counter])
                new_digit = digit * 2

                if new_digit >= 10:
                    even_total += ((new_digit % 10) + (new_digit // 10))
                else:
                    even_total += new_digit

            if counter % 2 != 0:
                digit = int(card_number[counter])
                odd_total += digit

        total_digits = even_total + odd_total
        if total_digits % 10 == 0:
            validity_status = "Valid"
        else:
            validity_status = "Invalid"

    return validity_status


def input_():
    global card_number

    user_card_number = input("Hello, Kindly enter card Details to verify: ")

    if re.search("^[0-9]+$", user_card_number):
        if 13 <= len(user_card_number) <= 16:
            card_number = user_card_number
            card_type_detector(user_card_number)
            card_validity_detector(user_card_number)

            print()
            print("*" * 40,
                  "\n**Credit Card Type: ", type,
                  "\n**Credit Card Number: ", user_card_number,
                  "\n**Credit Card Digit Length: ", len(user_card_number),
                  "\n**Credit Card Validity status: ", validity_status,
                  "\n", "*" * 40)
        else:
            print("Credit Card Number must be between 13 and 16")
            input_()
    else:
        print("Credit Card Number cannot be blank, contain letters or space. \nTry Again!")
        input_()


if __name__ == '__main__':
    input_()
