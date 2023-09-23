def fahrenheit(celsius):
    fahrenheit_value = (9 / 5) * celsius + 32
    return fahrenheit_value


print("fahrenheit\tcelsius")


for celsius in range(101):
    fahrenheit_value = fahrenheit(celsius)
    print(f"{celsius}\t{fahrenheit_value:.1f}")
