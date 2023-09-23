def product(*args):
    result = 1
    for number in args:
        if isinstance(number, int):
            result *= number
        else:
            print(f"Do not print non integer value{number}")
    return result


result1 = product(2, 3, 4, 5)
print("product1:", result1)

result2 = product(5, 6)
print("product2:", result2)

result3 = product(2, 3, 0, 4)
print("product3:", result3)
