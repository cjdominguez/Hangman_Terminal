

""""

hangman first push √
add read me file (uml included)
create basic structure
implement useful comments

to do:
        1. randomly choose a word from the word list and assign it to a variable -> chosen_word
        2. ask user to guess a letter and assign there letter (after lowercasing it) to a variable called -> guess
        3. check if the letter in guess is in chosen_word



"""
import random

wordlist = ["peaches", "dinosaur", "football", "apple"]

random.shuffle(wordlist)
for word in wordlist:
    chosen_word = word

guess = input("pick a lowercase letter...remember every wrong guess is a life!")

if guess.lower() in chosen_word:
    print(True)
else:
    print(False)





