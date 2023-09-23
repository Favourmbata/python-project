import random

number = random.randint(1, 1000)
guessTaken = 0
while guessTaken < 5:
    guess = input("Enter a guess")
    guess = int(guess)
    guessTaken = guessTaken + 1
    if guess < number:
        print("That is low")
    elif guess > number:
        print("That too high")
    else:
        break
if guessTaken == number:
    print("You won,Congratulation!")
else:
    print("You lost,Try harder.The right guess is", number)
