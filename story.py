def main():
    name = input("What is your name? ").strip().title()
    color = input("Color: ").strip().lower()
    adjective = input("Adjective: " ).strip().lower()
    goal = input("Goal: ").lower().strip()

    print("Hello ", name)

    print("This is your: ")

    print(f"At dawn the sky turned {color}, and the air felt {adjective}. I decided today I will finally {goal}.")

    print(f"At dawn the sky turned {color}, and the air felt {adjective}. I decided today I will finally {goal}.".upper())

    


main()
