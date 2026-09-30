

def main():

    not_validated = True

    while not_validated:
        try:
            num = int(input("Enter a number between 1 and 10: "))
            if num >= 1 and num <= 10:
                not_validated = False
            else:
                print("succes")
        except ValueError:
            print("You must enter a number between 1 and 10.")

    not_validated2 = True

    while not_validated2:
        try:
            name = input("Enter a name: ")
            if name == "":
                print("You must enter a name")
            else:
                not_validated2 = False
        except ValueError:
            print("You must enter a name")

    print(f"Stored name: {name}")






if __name__ == "__main__":
    main()
