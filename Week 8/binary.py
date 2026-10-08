list = [ ]

def binary_to_decimal(a):

    n = len(a)

    for i in range(n):
        num = a[i]
        print(num)
    for i in range(n):
        list.append(a[i])
    list.reverse()

    value = 0
    if list[0] == "1":
        value += 1
    if list[1] == "1":
        value += 2
    if list[2] == "1":
        value += 4
    if list[3] == "1":
        value += 8
    if list[4] == "1":
        value += 16
    if list[5] == "1":
        value += 32
    if list[6] == "1":
        value += 64
    if list[7] == "1":
        value += 128

    print(value)








def main():
    print("Binary to Decimal Converter")
    print("You type in Binary and Decimal comes out")

    b_num = input("Enter a binary number: ")

    binary_to_decimal(b_num)










main()
