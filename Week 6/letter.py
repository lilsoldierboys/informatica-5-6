names = ["mario", "luigi", "peach", "bowser", "Daisy", "Yoshi", "Toad", "Rosalina"]
sender = names[2]
num = 0
for i in range(len(names)):
    receiver = names[num]
    num += 1
    if receiver == "peach":
        receiver = names[num + 1]
    print(f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
       Dear {receiver},

       You are cordially invited to a ball at
       Peach's Castle this evening, 7:00 PM.

       Sincerely,
       {sender}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
""")



