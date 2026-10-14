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
#
#
#
#
import random
with open("words.txt") as new_file:
    content = new_file.read().splitlines()
word = random.choice(content)
print(word)
amount_l = len(word)
print(" _ "*amount_l)
