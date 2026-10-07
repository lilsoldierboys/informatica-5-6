def welcome():
    print("Welcome to Subway!")
    print("Here's the menu:\n1. Cheeseburger\n2. Fries\n3. Soda \n4. Ice Cream\n5. Cookie")

def get_item(a):
    items = ["🍔", "🍟", "🥤", "🍦", "🍪"]
    print(f"You chose a {items[a - 1]} ")



def main():
    welcome()
    item = input("What item would you like? ")
    if item == "1" or == "2" or == "3" or == "4" or == "5":
        item = int(item)
    elif item == "Cheeseburger":
        item = 1

    elif item == "Fries":
         item = 2
    elif item == "Soda":
        item = 3
    elif item == "Ice Cream":
         item = 4
    elif item == "Cookie":
         item = 5
    get_item(item)












main()
