def remove_Empty_strings(sample_input):
    return list(filter(None, sample_input))


def difference_of_numbers(numbers):
    max_val = max(numbers)
    min_val = min(numbers)

    difference = lambda x, y: x - y
    return difference(max_val, min_val)


def key_value_pair(input1, input2):
    result = dict(zip(input1, input2))
    return result
    # return {item1: item2 for value, (item1, item2) in enumerate(zip(input1, input2))}


from collections import Counter


def returns_frequency(result):
    k = 2
    res = [ele for ele, cnt in Counter(result).items() if cnt > k]

    return res


def splits_list(numbers):
    half = len(numbers) // 2
    return numbers[:half]


def convert_list_to_dictionary(input1):
    for word in range(len(input1) - 1):
        if input1[word][0] == input1[word + 1][0]:
            input1[word] = input1[word].capitalize()
    return input1


def list_to_dictionary(input1):
    return {input1[0]: input1 for index, input1 in enumerate(input1)}
