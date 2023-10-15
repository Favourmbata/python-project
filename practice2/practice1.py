user_input = int(input("Enter a number:"))

largest = user_input
smallest = user_input
average = user_input
total = user_input
product = user_input
count = 1

for num in range(3):
    user_input  = int(input("Enter a number:"))

    total += user_input
    product *= user_input
    count +=1
    if user_input < smallest:
        smallest = user_input

    if user_input > largest:
        largest = user_input

average = total / count
print(f'sum = {total}\nAverage: {average}\nproduct:{product}\nNumberOfStudent:{count}\nsmallest number:{smallest}\nlargestNumber:{largest}')
