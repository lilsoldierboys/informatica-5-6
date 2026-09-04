import random
import time




print("Welcome to HELL")


num1 = random.randint(10,99)
num2 = random.randint(10,99)

answ = int(input(f"{num1} + {num2} = "))

def add(num1,num2,answ):

    right = 0

    while right < 2:


        print(int(num1 + num2))

        if answ == int(num1 + num2):
            print("Correct")
            right += 1
            num1 = random.randint(10,99)
            num2 = random.randint(10,99)
            answ = int(input(f"{num1} + {num2} = "))
        elif answ != int(num1 + num2):
            print("Incorrect")
            right = 0
            num1 = random.randint(10,99)
            num2 = random.randint(10,99)
            answ = int(input(f"{num1} + {num2} = "))
add(num1,num2,answ)
