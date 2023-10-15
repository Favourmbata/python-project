number = [1, 2, 3, 4, 5]


def my_index(li: list, n):
    index = 0
    for i in range(len(li)):
        if li[i] == n:
            index = i
        break
    return index


print(my_index(number,3))

num = [2, 3, 4, 5, 6]


