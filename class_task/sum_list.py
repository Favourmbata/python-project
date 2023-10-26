# def sum_list(nexted_list):
#     total = 0
#     for numbers in nexted_list:
#         total += sum(numbers)
#         return total
#
#
# print(sum_list((2, 4, 5, 6,2, 3, 5, 6)))


# if __name__ == '__main__':

 # sum_list()
#
# print(sum_list(()))
sum_list = [[2, 4, 5, 6],[2, 3, 5, 6]]
# total = 0
# for number in sum_list:
#     for number1  in number:
#         total += number
# print(total)
#

a,b = sum_list
result = sum(a+ b)
print(result)