# item = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
# second_item = item[::2]
# print(second_item)

n = (('a', 23), ('b', 37), ('c', 11), ('d', 29))


def second_element(sup, item):
    return [sup[number::item] for number in range(item)]


print(second_element, (n, 2))



