list1 = [[1, 3], [5, 7], [9, 11]]
list2 = [[2, 4], [6, 8], [10, 12, 14]]
result = list(map(list.__add__, list1, list2))
print("\n Zipped list:\n" + str(result))
