to_do = []

print(f"tasks to do {len(to_do)}")
answ = input("Do you want to add a task? ")





while True:
    print(f"tasks to do {len(to_do)}")
    if answ == "remove":

        if answ == "complete all":
             to_do.clear()
        else:
            remove = input("What task do you want to remove? ")
            to_do.remove(remove)
            answ = input("Do you want to add, remove a task or exit? ")
        print(answ)
    elif answ == "exit":
        print(to_do)
        break



    elif answ == "y" or "add":
            print(to_do)
            x = input("Task you want to add: ")
            to_do.append(x)
            answ = input("Do you want to add, remove a task or exit? ")



