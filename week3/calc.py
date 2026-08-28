
eq = input(" ")

sep = eq.split(" ")

def add():
    answer = number1 + num2
    print(answer)

def sub():
    answer = number1 - num2
    print(answer)
def mult():
    answer = number1 * num2
    print(answer)
def div():
    if num2 != 0:
        answer = number1 / num2
        print(answer)



number1 = int(sep[0])

sign = sep[1]

num2 = int(sep[2])

if sign == "+":
    add()
elif sign == "-":
    sub()
elif sign == "/":
    div()
elif sign == "*":
    mult()





