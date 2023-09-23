def square(number):
    result = 0
    if number % 5 == 0:
        result = number ** 0.50
    else:
        result = number % 5
    return round(result,2)


print(square(5))
