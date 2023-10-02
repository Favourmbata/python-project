def largest_element(lit):
    largest = lit[0]
    for number in lit:
        if number > largest:
            largest = number
    return largest


print(largest_element([2, 3, 4, 10, 25]))



