import random

correct_answer = ["very Good", "nice work", "keep the Good work"]
incorrect_answer = ["no please try again", "Wrong please try again", "No keep trying"]


def computer_assisted_instruction():
    while True:
        response_type = random.randint(1, 3)
        if response_type == 1:
            response = random.choice(correct_answer)
        else:
            response = random.choice(incorrect_answer)

        print(response)

        user_input = input("Enter your response")
        if user_input.lower() == 'exist':
            break


if __name__ == '__main__':
    computer_assisted_instruction()


