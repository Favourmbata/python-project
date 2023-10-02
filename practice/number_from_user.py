summ = 0
largest = 0
for i in range(10):
    num = int(input("enter scores->"))
    summ += num
    if largest > num:
     print("The largest is ", largest)
print("The sum is ", summ)
