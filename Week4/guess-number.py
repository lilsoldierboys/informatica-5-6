import random


name = input("What´s your name? ")


print(f"Well, {name}, I am thinking of a number. Take a guess.")

dif = int(input("What difficulty? [1]Easy [2]Medium [3]Hard :"))


def easy():
    print("Im thinking of a number from 1 to 20")

    numb = random.randint(1,20)

    guess = int(input("What is my number? "))

    attempts = 0

    while attempts < 7:
        if guess > numb:
            print("Your guess is too high.")
            print("Take a guess.")
            guess = int(input("What is my number? "))
            attempts += 1
        elif  guess < numb:
            print("Your guess is too low.")
            print("Take a guess")
            guess = int(input("What is my number? "))
            attempts += 1
        elif  guess == numb:
            print(f"Good job, {name} You guessed my number!")
            break
        print("you ran out of atempts")


def medium():
    print("Im thinking of a number from 1 to 50")

    numb = random.randint(1,50)

    guess = int(input("What is my number? "))

    attempts = 0

    while attempts < 5:
        if guess > numb:
            print("Your guess is too high.")
            print("Take a guess.")
            guess = int(input("What is my number? "))
            attempts += 1
        elif  guess < numb:
            print("Your guess is too low.")
            print("Take a guess")
            guess = int(input("What is my number? "))
            attempts += 1
        elif  guess == numb:
            print(f"Good job, {name} You guessed my number!")
            break
        print("you ran out of atempts")
def hard():
    print("Im thinking of a number from 1 to 100")

    numb = random.randint(1,100)

    guess = int(input("What is my number? "))

    attempts = 0

    while attempts < 3:
        if guess > numb:
            print("Your guess is too high.")
            print("Take a guess.")
            guess = int(input("What is my number? "))
            attempts += 1
        elif  guess < numb:
            print("Your guess is too low.")
            print("Take a guess")
            guess = int(input("What is my number? "))
            attempts += 1
        elif  guess == numb:
            print(f"Good job, {name} You guessed my number!")
            break
        print("you ran out of atempts")




if dif == 1:
    easy()
elif dif == 2:
    medium()
elif dif == 3:
    hard()




