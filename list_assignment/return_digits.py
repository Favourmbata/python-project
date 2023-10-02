def return_digits(number_1):
    digit = str(number_1)
    digit_lst = []
    for i in range(len(digit)):
        digit_lst.append(int(digit[i]))
    return digit_lst


number = input("Enter the number:")
list_digits = return_digits(number)
print(list_digits)