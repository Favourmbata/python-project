# item = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
# second_item = item[::2]
# print(second_item)


tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
tuple1 = tuple(sorted(list(tuple1), key=lambda x: x[1]))
print(tuple1)
