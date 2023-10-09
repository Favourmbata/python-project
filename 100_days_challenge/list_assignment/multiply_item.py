def multiply(lst):
    multiplication = 1
    for i in lst:
        multiplication *= i
    return multiplication


print(multiply([15, 20, 25, 20, 10, 5]))


lst = [15, 20, 25, 20, 10, 5]

multiply = []
for i in lst:
    multiply.append(i*2)
print(multiply) 