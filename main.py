""""
Christian Dominguez
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

HIDDEN_WORDS = ["purple", "orange", "family", "apples", "banana"]
chosen_word = random.choice(HIDDEN_WORDS)
end_of_game = False
lives = len(chosen_word)

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

print(f"psst a hint to solution -> {chosen_word}")

#spaces
display = []
for spaces in range(len(chosen_word)):
    """
    crucial to use len because otherwise replacing with letter is not possible 
    """ 
    display.append("_")

while not end_of_game:
    """
    while loop runs until end_of_game turns TRUE
    """
    guess = input("Guess a letter: ").lower()
    counter = 0
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives-=1
        if lives == 0:
            end_of_game = True
            print("You Lose")
     
    if '_' not in display:
        end_of_game = True  
        print("You Win.")

    print(" ".join(display),f" You have {lives} left. ")
    print(stages[lives])



    




