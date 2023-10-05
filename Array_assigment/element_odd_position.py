def return_odd_position(list_position):
    c = []
    for i in range(1, len(list_position), 2):
        c.append(lst[i])
    return c


lst = [2, 4, 23, 14, 54, 90, 110, 33]

odd_element = return_odd_position(lst)
print(odd_element)

