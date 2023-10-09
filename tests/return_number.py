def get_extra_number(total):
    lst = []
    for number in total:
        if total.count(number) > 1:
            lst.append(number)
    return tuple(sorted(set(lst)))


def get_reversed_element(solution):
    lst = []
    for number in range(len(solution)):
        lst.append(solution[-(number + 1)])
    return tuple(lst)


def get_nested_element(number):
    special_item = []


pass


def get_swapped_element(item):
    lt = list(item)
    lt[0], lt[7] = lt[7], lt[0]
    lt.append(item)
    new_list = lt[0], lt[7]
    return tuple(new_list)


def get_second_item(number):
    pass
