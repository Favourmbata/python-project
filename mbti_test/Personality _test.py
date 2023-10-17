extrovertCount = 0
introvertCount = 0

sensitiveCount = 0
intuitiveCount = 0

thinkerCount = 0
feelerCount = 0

judgingCount = 0
perspectiveCount = 0

answers = []
username = ""

questions = [
    ["A. Expend energy, enjoy groups.", "B. Conserve energy, one-on-one"],
    ["A. Interpret literally. ", "B. Look for meaning and possibilities"],
    ["A. Logical, thinking, questioning.", "B. Empathetic, feeling, accommodating"],
    [" A. Organized, orderly. ", "B. Flexible, adaptable"],
    [" A. More outgoing, think out loud.", "B. More reserved, think to yourself."],
    [" A. Practical, realistic, experiential.", "B. Imagination, innovative, theoretical."],
    [" A. Candid, straight forward, frank.", "B. Tactful, kind, encouraging."],
    [" A. Plan, schedule. ", "B. Unplanned, spontaneous"],
    [" A. Seek many tasks, public activities, interaction with others.", "B. Seek private, solitary activities with "
                                                                         "quiet to concentrate."],
    ["A. Standard, usual, conventional.", "B. Different, novel, unique."],
    ["A. Firm, tend to criticize, hold the line.", "B. Gentle, tend to appreciate, conciliate."],
    [" A. Regulated, structured.", "B. Easygoing, live and let live."],
    [" A. External, communicative, express yourself.", "B. Internal, reticent, keep to yourself."],
    [" A. Focus on here-and-now. ", "B.Look to the future, global perspective, big picture"],
    [" A. Tough minded, just.  ", "B. Tender-hearted, merciful"],
    [" A. Preparation, plan ahead. ", "B. Go with the flow, adapt as you go."],
    [" A. Active, initiate.", " B.Reflective, deliberate"],
    [" A. Facts, things, what is.", "B. Ideas, dreams, 'what could be', philosophical"],
    [" A. Matter of fact, issue oriented.", "B. Sensitive, people-oriented, compassionate"],
    [" A. Control, govern. ", "B. Latitude, freedom"]
]

counting_variable = 0


def input_collection():
    global counting_variable
    for counter in range(counting_variable, len(questions)):
        if counting_variable == 20: break
        print(questions[counter])
        try:
            user_input = input("Enter your choice: ")
            user_input = user_input.lower()
            if user_input == 'a' or user_input == 'b':
                counting_variable += 1
                answers.append(user_input)
                accept_inputs(user_input, counter)
                print(counting_variable)
            else:
                raise ValueError("Invalid input")

        except ValueError as error:
            print(error)
            input_collection()


def accept_inputs(user_input: str, counter: int):
    global extrovertCount, introvertCount, sensitiveCount, intuitiveCount, thinkerCount, \
        feelerCount, judgingCount, perspectiveCount

    introvert_extrovert(counter, user_input)

    sensitive_intuitive(counter, user_input)

    thinker_and_feeler_counter(counter, user_input)
    judging_and_perspective_counter(counter, user_input)


def introvert_extrovert(counter, user_input):
    global extrovertCount, introvertCount
    if counter == 0 or counter == 4 or counter == 8 or counter == 12 or counter == 16:
        if user_input == "a":
            extrovertCount += 1
        else:
            introvertCount += 1


def sensitive_intuitive(counter, user_input):
    global sensitiveCount, intuitiveCount
    if counter == 1 or counter == 5 or counter == 9 or counter == 13 or counter == 17:
        if user_input == "a":
            sensitiveCount += 1
        else:
            intuitiveCount += 1


def thinker_and_feeler_counter(counter, user_input):
    global thinkerCount, feelerCount
    if counter == 2 or counter == 6 or counter == 10 or counter == 14 or counter == 18:
        if user_input == "a":
            thinkerCount += 1
        else:
            feelerCount += 1


def judging_and_perspective_counter(counter, user_input):
    global judgingCount, perspectiveCount
    if counter == 3 or counter == 7 or counter == 11 or counter == 15 or counter == 19:
        if user_input == "a":
            judgingCount += 1
        else:
            perspectiveCount += 1


def personality_test():
    input_collection()


def print_answer():
    global answers

    for counter in range(0, len(answers), 4):
        if answers[counter] == 'a':
            print(questions[counter][0])
        else:
            print(questions[counter][1])
    print("Number of A selected: ", extrovertCount, "\nNumber of B selected: ", introvertCount)
    print()

    for counter in range(1, len(answers), 4):
        if answers[counter] == 'a':
            print(questions[counter][0])
        else:
            print(questions[counter][1])
    print("Number of A selected: ", sensitiveCount, "\nNumber of B selected: ", intuitiveCount)
    print()

    for counter in range(2, len(answers), 4):
        if answers[counter] == 'a':
            print(questions[counter][0])
        else:
            print(questions[counter][1])
    print("Number of A selected: ", thinkerCount, "\nNumber of B selected: ", feelerCount)
    print()

    for counter in range(3, len(answers), 4):
        if answers[counter] == 'a':
            print(questions[counter][0])
        else:
            print(questions[counter][1])
    print("Number of A selected: ", judgingCount, "\nNumber of B selected: ", perspectiveCount)
    print()


def collate():
    personality = ""
    if extrovertCount > introvertCount:
        personality += "E"
    else:
        personality += "I"

    if sensitiveCount > intuitiveCount:
        personality += "S"
    else:
        personality += "N"

    if thinkerCount > feelerCount:
        personality += "T"
    else:
        personality += "F"

    if judgingCount > perspectiveCount:
        personality += "J"
    else:
        personality += "P"

    print("Your personality is: ", personality)


def name_input():
    global username
    username = input("Enter your name: ")


def print_name():
    print("\nHello ", username, "You selected ")


if __name__ == '__main__':
    name_input()
    personality_test()
    print_name()
    print_answer()
    collate()
