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


def pick_word():
    """
    this function randomly chooses a word from the word bank below and returns it
    """

    HIDDEN_WORDS = ["peaches", "dinosaur", "football", "apple"]
    random.shuffle(HIDDEN_WORDS)

    for word in HIDDEN_WORDS:
        chosen_word = word
        print(chosen_word)
        return chosen_word


# aaa
def clean_input():
    """
    clean the input string by lower-casing the input
    then,
    check if input is the correct type -> A - Z characters only..
    """
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    guess_char = guess.lower()
    if guess_char in alphabet:
        return guess_char
    else:
        print("Invalid Input")


def check_input():
    """
    checks if user input is correct or not
    """
    counter = 0
    for letter in secret_word:
        if letter == user_char:
            counter += 1
    if counter <= 0:
        return False


def display_rules():
    """
    display/explain rules to user in terminal
    """
    print("\nWelcome to Christian Dominguez's version of Hangman \n "
          "The rules are simple:\n"
          "1. You get 12 guesses\n"
          "2. The word will be reveled at the end, WIN or lose.\n"
          "3. any character/input not in the alphabet is INVALID"
          "\n\n")


def gameplay():
    pass


display_rules()
guess = input("Pick a lowercase letter to start with...remember every wrong guess is a life! \n")
secret_word = pick_word()  # return value from pick_word function
user_char = clean_input()  # return value from clean_input function
check_input()
