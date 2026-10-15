#define main()
#   print("A welcome")
#   pull possible words from a list using random assign to a var
#define the hangman function(a) with a parameter
#   seperate the chosen word into its letters
#   ask user for a letter
# make sure they input a letter
#use a for in check a list with all letters in the alphabet
#use .lower
#
#in a while loop
#   check if letter is in the word if not take one of the 5 tries
#   stored in a var
#   if it is tell them
#   check position iin word of letters
# show print(list[correct])
#   repeat
# if the user gets it in the proper tries print congrats
# break the loop
#if not print they lose
#ask if they want to play again
#
#
#
#
#run main and put word in hangman parameters
#
#
#
#

import random




with open("words.txt") as new_file:
    content = new_file.read().splitlines()
word = random.choice(content)
print(word)
word = word.lower()
ats = 10

hint = ["_"] * len(word)
inco_w = [" "]


while ats > 0:
    print(" ".join(hint))

    att = input("Enter guess: ").lower()


    if att in word and att not in hint:
        for letter in range(len(word)):
            if word[letter] == att:
                hint[letter] = att
        print("Great guess!")
        print(" ".join(hint))
    elif att in hint:
        print("Already guessed that one")

    else:
        print("incorrect")
        inco_w.append(att)
        print(" ".join(inco_w))
        ats -= 1
        print(f"Attempts: {ats}")

    if "_" not in hint:
        final = ("".join(hint))
        print(f"You did it you guessed the word the word was: {final}")
        break
