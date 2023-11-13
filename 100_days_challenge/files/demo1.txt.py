try:
    with open("demo.txt", mode='r') as datas:
        for data in datas:
            a, *b = data.split()
            print(a, *b)


except FileNotFoundError:
    print("make sure you check your file spelling")

print("program exception continues....")
