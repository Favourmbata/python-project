# number = input("Enter a number->")
# reverse = number[::-1]
# if number == reverse:
#     print("True")
# else:
#     print("False")


def is_palindrome(number):
    num = number
    reverse = 0
    while number != 0:

        reverse = reverse * 10 + number % 10
        number = number // 10

    if num == reverse:
        return True
    else:
        return False


print(is_palindrome(121))
