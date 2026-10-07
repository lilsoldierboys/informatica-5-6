print("Welcome to the times table quiz")
dang1 = True
dang2 = True
dang3 = True
while dang1:
    try:
        init = int(input("What table do you want to be tested on: "))
        dang1 = False
    except ValueError:
        print("Enter a number")
        init = int(input("What table do you want to be tested on: "))
while dang2:
    try:
        max_value = int(input("Until what number do you want o be quizzed: "))
        dang2 = False
    except ValueError:
        print("Enter a number")
        max_value = int(input("Until what number do you want o be quizzed: "))
start = str(init)
tab = int(init)
num = 1
wrong = 0
good = True

while good:
    tab = int(init)
    if tab <= 10:
        for i in range(max_value):
            print(f"You will be tested on the {tab} table")
            print(f"{start} times {num} is..")
            while dang3:
                try:
                    user_input = int(input("Answer: "))
                    dang3 = False
                except ValueError:
                    print("Input a number")
                    user_input = int(input("Answer: "))

            dang3 = True
            if user_input == (tab * num):
                print("Correct")
                num += 1
            else:
                print("Incorrect")
                wrong += 1
                num += 1
    good = False


print(f"You got {num - 1 - wrong} right out of {num - 1}")

        #
           # try:
            #
               # print("Enter a number")
