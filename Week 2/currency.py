    #184.01
    #3132.14
    #0.20
    #3.37
    #0.31
    #5.22
def main():
    c_pesos = float(input("What do you have left in pesos? "))
    soles = float(input("What do you have left in soles? "))
    reals = float(input("What do you have left in reals? "))

    Pesos = (soles * 0.20) + (reals * 0.31) + (c_pesos * 184.01)

    Pesos = round(Pesos, 2)

    USD = Pesos * 0.059

    USD = round(USD, 2)

    print("USD: ", USD )
    print("Pesos: ", Pesos)

main()
