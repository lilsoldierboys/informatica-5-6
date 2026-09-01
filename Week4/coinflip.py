import random

a = 0
while a < 3:

    guess = input("Heads or Tails: ").lower().strip
    coin = ["heads", "tails"]
    outcome = random.choice(coin)

    if outcome == "heads":
        print("heads")
    elif outcome == "tails":
        print("tails")

    if guess == outcome:
        print("You win!")
        break
    elif guess != outcome:
        print("You lose :(")


    a += 1





