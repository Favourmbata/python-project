# sample_input = ["", 'ABC', 'xyz', "", 'abc', 'XYZ']

# list1 = [",'ABC','xyz',", 'abc', 'XYZ']
# sample_input = list(filter(None, sample_input))
# # print(str(sample_input))
# test_list = ["", 'ABC', 'xyz', "", 'abc', 'XYZ']
#
# test_list = [i for a, i in enumerate(test_list) if i != '']
#
# print(test_list)
#
# sample_input = [i for i, i in enumerate(sample_input) if i != " "]
# print(sample_input)
# character = ['apple', 'banana', 'coconut']
# items = character.items()
#


# list1 = ['a', 'b', 'c', 'd', 'e']
# list2 = [1, 2, 3, 4, 5]
# res = {}
# for key in list1:
#     for value in list2:
#         res[key] = value
#         list2.remove(value)
#         break
# print(str(res))

#
# list1 = ['a', 'b', 'c', 'd', 'e']
# list2 = [1, 2, 3, 4, 5]
# res = dict(zip(list1,list2))
# print(str(res))

# sample_list = [10, 75, 20, 30, 15, 5, 40, 25, 40, 35]
# max_val = sample_list[0]
# min_val = sample_list[0]
#
# for i in range(1, len(sample_list)):
#     if sample_list[i] > max_val:
#         max_val = sample_list[i]
#     elif sample_list[i] < min_val:
#         min_val = sample_list[i]
# print("The difference between largest and smallest is: " + str(max_val - min_val))
# max_value = max(sample_list)
# min_value = min(sample_list)
# difference = lambda x, y: x - y
# print("the difference is ", difference(max_value, min_value))
# array_nums = [5, 7, 2, 4, 9]
# print("Original Array:", array_nums)

# max_val = max(sample_list)
# min_val = min(sample_list)
#
# difference = lambda x, y: x - y
#
# print("Difference between the largest and smallest values of the said array:", difference(max_val, min_val))


# unique_element = []
# frequency = {}
# output = []
# for i in sample_input:
#     if i not in unique_element:
#         unique_element.append(i)
#         frequency[i]= 1
#     else:
#         frequency[i] +=1
#         if frequency[i] == k + 1:
#             output.append(i)
#             print(str(output))
#
# from collections import Counter
#
# sample_input = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 5, 5, 5, 6, 7]
# k = 2
#
# # using list comprehension to bind result
# res = [ele for ele, cnt in Counter(sample_input).items() if cnt > k]
# #
# # printing results
# print("The required elements : " + str(res))
# def split_two_parts(list1, l):
#     return list1[::l], list1[l:]
#
#
# list1 = [10, 75, 20, 30, 15, 5, 40, 25, 40, 35]
# first_list_length = 2
# print(split_two_parts(list1, first_list_length))
#
#


# def convert(list1):
#     rest = map(lambda i: (list1[i], list1[i + 1]), range(len(list1) - 1)[::2])
#     return dict(rest)
#
#
# list1 = ['a', 1, 'b', 2, 'c', 3]
# print(convert(list1))

# key1 = ['apple', 'banana', 'coconut']
# for i in key1.


def split(number):
    half = len(number) // 2
    return number[:half], number[half:]


a = [10, 75, 20, 30, 15, 5, 40, 25, 40, 35]
b, c = split(a)

print(split())
