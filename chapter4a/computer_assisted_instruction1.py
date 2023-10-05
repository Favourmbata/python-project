import random


def multiplication():
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    return num1, num2


def main():
    while True:
        num1, num2 = multiplication()
        correct_answer = num1 * num2

        while True:
            user_input = int(input(f' how much is {num1} times {num2} ?:'))
            if user_input == correct_answer:
                print("very good")
                break
            else:
                print(" No please try again ")
        another_question = input("Do you want try another question (yes/no)")
        if another_question.lower() != 'yes':
            print("Bye for now ->")
            break


if __name__ == '__main__':
    main()