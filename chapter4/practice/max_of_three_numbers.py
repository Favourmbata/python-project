def tw0_number(num1, num2):
    if num1 > num2:
        return num1
    return num2


def three_number(num1, num2, num3):
    return tw0_number(num1, tw0_number(num2, num3))


print(three_number(3, 6, 9))
