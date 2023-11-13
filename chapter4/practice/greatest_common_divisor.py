def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return b
    if a > b:
        return gcd(a - b, b)
    return gcd(a, b - a)


if __name__ == '__main__':
    a = 105
    b = 252
    if gcd(a, b):
        print("The gcd of", a, " and ", b, " is ", " = ", gcd(a, b))
    else:
        print("not found")

