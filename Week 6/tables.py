
init = int(input("What table do you want to learn: "))
start = str(init)
tab = int(init)
num = 1

while start != "exit" and tab <= 10:
    tab = int(init)
    for i in range(10):
        print(f"{start} times {num} is {tab * num}")
        num += 1
    num = 1
    init = input("What table do you want to learn: ")
    start = str(init)




