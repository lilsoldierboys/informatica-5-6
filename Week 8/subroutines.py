def main():

    def calculate(a, b):
        answer = a + b
        print(f"{a} + {b} = {answer}")


    num1 = 10
    num2 = 15

    calculate(num1, num2)


    def average_value(a, b, c):
        average = (a + b + c)/3
        print(f"The average is {average}")



    num1 = int(input("Number 1: "))
    num2 = int(input("Number 2: "))
    num3 = int(input("Number 3: "))

    average_value(num1, num2, num3)

if __name__ == "__main__":
    main()
