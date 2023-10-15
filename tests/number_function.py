def exercise1():
    return list(range(1, 21))

    #  return [number for number in list1 if number % 2 != 0]


def exercise2(list1):
    res = []
    for number in list1:
        if number % 2 == 1:
            res.append(number)
    return res


def exercise3(list1):
    answer = []
    for number in list1:
        if number % 2 == 1:
            answer.append(number * 2)
    return answer

    # return [i * 2 for i in list1 if i % 2 == 1]


def exercise4(list1):
    result = [i * 2 for i in list1 if i % 2 == 1]
    result[4:8] = [0] * len(list1[4:8])
    return result


def exercise5(list1,list2):
    return [x + y for x,y in zip(list1,list2)]
