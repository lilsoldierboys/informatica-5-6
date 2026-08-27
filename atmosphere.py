
layer = input("Atmoshpere Descent Layer: ").lower().strip()


def therm():
    print("Your altitude level will be between 700–10,000 km")
    exact_h = int(input("Exact altitude: "))

if exact_h >= 85000 and exact_h <= 700000:
        t_i_l = exact_h - 85000
        speed2 = t_i_l / 500
        print(speed2)
        exact_h -= t_i_l
        if exact_h >= 50000 and exact_h <= 85000:
            t_i_l = exact_h - 50000
            speed3 = t_i_l / 200
            print(speed3)
            exact_h -= t_i_l
            print(exact_h)
            if exact_h >= 12000 and exact_h <= 50000:
                t_i_l = exact_h - 12000
                speed4 = t_i_l / 200
                print(speed4)
                exact_h -= t_i_l
                if exact_h >= 1 and exact_h <= 12000:
                    speed5 = exact_h / 20
                    time = speed1 + speed2 + speed3 + speed4 + speed5
                    print(f"{time} seconds")
def exo():
    print("Your altitude level will be between 700–10,000 km")
    exact_h = int(input("Exact altitude: "))
    exact_h *= 1000
    if exact_h > 700000:
        t_i_l = exact_h - 700000
        speed1 = t_i_l / 2000
        print(speed1)
        exact_h -= t_i_l
        if exact_h >= 85000 and exact_h <= 700000:
            t_i_l = exact_h - 85000
            speed2 = t_i_l / 500
            print(speed2)
            exact_h -= t_i_l
            if exact_h >= 50000 and exact_h <= 85000:
                t_i_l = exact_h - 50000
                speed3 = t_i_l / 200
                print(speed3)
                exact_h -= t_i_l
                print(exact_h)
                if exact_h >= 12000 and exact_h <= 50000:
                    t_i_l = exact_h - 12000
                    speed4 = t_i_l / 200
                    print(speed4)
                    exact_h -= t_i_l
                    if exact_h >= 1 and exact_h <= 12000:
                        speed5 = exact_h / 20
                        time = speed1 + speed2 + speed3 + speed4 + speed5
                        print(f"{time} seconds")

def three()
    if exact_h >= 85000 and exact_h <= 700000:
                t_i_l = exact_h - 85000
                speed2 = t_i_l / 500
                print(speed2)
                exact_h -= t_i_l
                if exact_h >= 50000 and exact_h <= 85000:
                    t_i_l = exact_h - 50000
                    speed3 = t_i_l / 200
                    print(speed3)
                    exact_h -= t_i_l
                    print(exact_h)
                    if exact_h >= 12000 and exact_h <= 50000:
                        t_i_l = exact_h - 12000
                        speed4 = t_i_l / 200
                        print(speed4)
                        exact_h -= t_i_l
                        if exact_h >= 1 and exact_h <= 12000:
                            speed5 = exact_h / 20
                            time = speed1 + speed2 + speed3 + speed4 + speed5
                            print(f"{time} seconds")




if layer == "Thermosphere":
    therm()
elif layer == "Exosphere":
    exo()
elif layer == "Mesosphere":
    three()
elif layer == "Stratosphere":

                        if exact_h >= 12000 and exact_h <= 50000:
                            t_i_l = exact_h - 12000
                            speed4 = t_i_l / 200
                            print(speed4)
                            exact_h -= t_i_l
                            if exact_h >= 1 and exact_h <= 12000:
                                speed5 = exact_h / 20
                                time = speed1 + speed2 + speed3 + speed4 + speed5
                                print(f"{time} seconds")
elif layer == "Troposphere":
     if exact_h >= 1 and exact_h <= 12000:
        speed5 = exact_h / 20
        time = speed1 + speed2 + speed3 + speed4 + speed5
        print(f"{time} seconds")


