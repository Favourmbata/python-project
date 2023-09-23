import random
number = random.randint(1,1000)
guessTaken = 0
while guessTaken < 10:
    guess = input("Enter a guess")
    guess = int(guess)
    guessTaken = guessTaken +1
    if guess < number:
        print("That was too low")
    elif guess > number:
        print("That was too high")
    else:
        break
if guessTaken == number:
    print("Either you know the secret or you got lucky!")
else:
    print("You should be able to do better!The right number is:",number)