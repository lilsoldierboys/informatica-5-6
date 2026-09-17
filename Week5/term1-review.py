from datetime import datetime


def main():
    day = datetime.now().weekday()



    if day < 4:
        print("Its a weekday")
        remaining = 5 - day
        print(remaining, "days until the weekend")
    elif day == 4:
        print("Its Friay")
        print("Just a day left until the weekend")
    else:
        print("Its the weekend")





if __name__ == "__main__":
    main()


days = ["monday", "tuesday", "thursday", "friday", "saturday", "sunday"]


print(days[0])



months = ["January", "february", "march", "april", "may", "june", "july", "august", "september", "october", "November", "december"]

#print("These are the summer months:")
#print(months[5])
#print(months[6])
#print(months[7])

month = datetime.now().month
seasons = ["winter", "Spring", "Summer", "Autumn"]

if month <= 2 or month == 12:
    season = 0
elif month <= 5:
    season = 1
elif month <= 8:
    season = 2
else:
    season = 3

print("It is", seasons[season])


print("It is", months[month-1])
