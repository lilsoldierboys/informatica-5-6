import random

guess = int(input("Heads or Tails: "))

outcome = random.randint(1,2)

if outcome == 1:
    print("Heads")
elif outcome == 2:
    print("Tails")

if guess == outcome:
    print("You win!")
elif guess != outcome:
    print("You lose :(")
else:
    print("invalid choice")







