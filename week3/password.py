import getpass


password = input("Password: ")

secret = getpass.getpass("What is your password: ")

if secret == password:
    print("Correct Password")
else:
    print("Wrong")
