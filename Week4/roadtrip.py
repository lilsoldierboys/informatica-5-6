import time

answ = ""


while answ != "yes":
    time.sleep(1.5)
    answ = input("Are we there yet? ").lower().strip()


