# employee = ("Orange", [10, 20, 30], (5, 15,25))
# print(employee.index([10, 20, 30]), employee.index((5, 15, 25)),employee.index("Orange"))


tup = ("Orange", [10, 20, 30], (5, 15, 25))
x = []
for number in tup:
    x.extend(number)
# print(x)
#
# tup = (['a', 'apple'], ['b', 'ball'])
# x = []
# for i in tup:
#     x.extend(i)
# print(x)
#
# test_list = [(4, (5, 'Gfg')), (7, (8, 6))]
#
# # printing original list
# print("The original list is : " + str(test_list))
#
# # Unpacking nested tuples
# # using list comprehension
# res = [(x, y, z) for x, (y, z) in test_list]
#
# # printing result
# print("The unpacked nested tuple list is : " + str(res))
#
# tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
# (fruit, lst1, tpl) = tuple1
# lst2 = []
# lst3 = []
# lst2.append(lst1.index(lst1[1]) - 1)
# lst2.append(lst1[1])
# lst3.append(tpl.index(tpl[2]) - 1)
# lst3.append(tpl[2])
# combined = [tuple(lst2), tuple(lst3)]
# print(tuple(combined))

#
# tuple1 = (10,20,30,40,50)
# tuple1 = tuple1[::-1]
# print(tuple1)


# tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
# print(tuple1[1][1])
#
# numbers = [1, 2, 3, 4, 5, 6]
# numbers *= 2
# print(numbers)


u = (2,4,6)
y = (2,4,5)
sum = u + y
print(sum)
