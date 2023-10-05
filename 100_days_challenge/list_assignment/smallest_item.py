def smallest(item):
    smallest_element = item[0]
    for x in item:
        if x < smallest_element:
            smallest_element = x
    return smallest_element


print(smallest([15, 20, 25, 20, 10, 5]))
