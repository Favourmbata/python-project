# def non_negative_integer(number, letter):
#     number = int(input("enter a number:"))
#
#
# letter = int(input("enter a string number:"))
# if len(letter <= 2):
#     print(letter)
#



def letter_print():
    word = input("Enter a Word: ")
    try:
        number = int(input("Enter a number: "))
        if len(word) < 2:
            print(f"{word}\n" * number)
        else:
            print(f"{word[0]} {word[1]}\n" * number)
    except ValueError:
        print("Only numbers are Accepted")


if __name__ == '__main__':
    letter_print()