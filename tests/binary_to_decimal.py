bin = input("enter a number: ")
def binary(bin):
    decimal = 0
    for i in bin:
        decimal = decimal * 2 + int(i)

    print("binary to decimal is: ",decimal)
 
binary(bin)
