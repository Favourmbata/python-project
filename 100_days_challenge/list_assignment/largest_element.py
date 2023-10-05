def largest_element(lit):
    largest = lit[0]
    for number in lit:
        if number > largest:
            largest = number
    return largest


print(largest_element([15, 20, 25, 20,10, 5]))



