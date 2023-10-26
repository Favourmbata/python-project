def get_binary_value(number):
    if number > 1:
        get_binary_value(number // 2)
    return number % 2,


num = int(input("num: "))
bin = get_binary_value(num)
