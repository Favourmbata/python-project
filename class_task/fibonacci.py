# first_term = 0
# second_term = 1
# third_term = 1
#
# print(first_term, " ", second_term)
# for number in range(0, 50):
#     if number < 50:
#         print(second_term)
#     third_term = first_term + second_term
#     print(third_term)
#     first_term = second_term
#     second_term = third_term
#     print()

# number1 = 0
# number2 = 1
# num3 = number1 + number2
# while number1 < 50:
#     print(number1, end=" ")
#     number1 = number2
#     number2 = num3
#     num3 = number1 + number2


first_number = 0
second_number = 1
third_number = first_number + second_number
for number1 in range(50):
    print(first_number,end=" ")
    first_number = second_number
    second_number = third_number
    third_number = first_number + second_number
