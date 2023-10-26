def get_biggest_odd(list_odd):
    largest_odd = '0'
    for num in list_odd:
        if num > largest_odd:
            largest_odd = num
    return largest_odd


def get_bigger_odds(numbers):
    return int(max(number for number in numbers if int (number % 2 == 1)))