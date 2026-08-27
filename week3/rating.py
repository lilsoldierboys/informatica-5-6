rating = float(input("Rate the restaurant "))

if rating > 5:
    print("Nonvalid")
if rating >= 4.5 and < 5:
    print("Perfect")
if rating >= 4.0 and < 4.5:
    print("Good")
if rating >= 3.0 and < 4:
    print("decent")
if rating >= 2 and < 3:
    print("fair")
else:
    print("Terrible")
