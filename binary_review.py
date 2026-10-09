

def binary_to_decimal(a):


    value = 0
    for bit in a:
        value = (value * 2) + int(bit)


    print(f"Decimal value: {value}")


def main():
    print("Binary to Decimal Converter")
    print("You type in Binary and Decimal comes out")

    valid_bits = ["0","1"]

    while True:
        b_num = input("Enter a binary number: ")

        valid_input = 0

        for input_bit in b_num:
            if input_bit in valid_bits:
                valid_input += 1
        if valid_input == len(b_num):
            break
        else:
            print("Invalid")




    binary_to_decimal(b_num)










main()
