
def highest(a, b):
    highest_num = 0
    if a > b:
        highest_num = a
    else:
        highest_num = b
    print(f"The biggest number is {highest_num}")


num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))


highest(num1, num2)

def lowest(a, b, c):
    low_val = 0
    if a < b and a < c:
        low_val = a
    elif b < a and b < c:
        low_val = b
    elif c < b and c < b:
        low_val = c
    print(f"The smallest number is {low_val}")


num3 = int(input("Enter number 1: "))
num4 = int(input("Enter number 2: "))
num5 = int(input("Enter number 3: "))


lowest(num3, num4, num5)
