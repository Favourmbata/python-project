def add_function(numbers: list):
    sums = 0
    for i in numbers:
        sums += i
    return sums


def multiply_function(numbers: list):
    multiply = 1
    for total in numbers:
        multiply *= total
    return multiply


def largest_function(numbers: list):
    largest = 0
    for number in numbers:
        if number > largest:
            largest = number
    return largest


def smallest_function(numbers: list):
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest


def no_duplicate(numbers):
    unique_value = []
    for number in numbers:
        if number not in unique_value:
            unique_value.append(number)
    return unique_value


def triple_element(numbers):
    tripled_value = []
    for number in numbers:
        tripled_value.append(number ** 3)
    return tripled_value
