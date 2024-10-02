"""
    Hangman Game (using Python 3.12.5)

"""

from random2 import choice
from colorama import Fore, init, Style
from pyfiglet import  Figlet

init()

words = ['apple', 'banana', 'orange', 'grape', 'kiwi']
guessed_letters = []
correct_letters = []
word_letters = []
attempts = 6
count = 0

hangman_draw = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
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
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def choose_word():
    '''
    This function randomly chooses a word from the list of words. It also takes makes a list of letters from the chosen word (it shouldn't contain the duplicates).
    The return values are the word and the list of letters.
    '''

    word = choice(words)
    word_letters = list(word)
    return word, word_letters


def display_word(word, correct_guesses):
    '''
    This function takes in a word and a list of guessed letters, and returns a string that represents the word with the guessed letters revealed. It takes as input the word and a list of guessed letters.
    '''

    revealed = ' '.join([letter if letter in guessed_letters else '_' for letter in word])
    print(f"{revealed}")



def hangman():
    global  count
    figlet = Figlet(font='slant')
    text_art = figlet.renderText('Hangman_Game')
    print(hangman_draw[count])

    global  attempts
    word, word_letters = choose_word()

    print("\t \t \t", text_art )

    print("word chosen by computer:" , word)
    #print("letters:" , word_letters)

    display_word(word, guessed_letters)

    # Check if the guess is a single letter - if not, print out to the user to use only single letters and go for the next guess
    # Check if the guess is not a letter - if so, print out to the user that it is not a letter and go for the next guess
    while attempts > 0:
        guess = input("Guess a letter: ").lower().strip()
        print(guess)

        if  len(guess) != 1:
            print(Fore.RED,"Multiple char or word now allowed . please enter only single letter", Style.RESET_ALL)
            #guess = input("Guess a letter: ").lower().strip()
            continue
            # Check if the guess is a letter (alphabet)
        if not guess.isalpha():
                print(Fore.RED,"That is not a letter. Please guess a valid letter.")
                continue

            # Check if the letter has been guessed already
        if guess in guessed_letters:
                print(Fore.BLUE, f"You've already guessed the letter '{guess}'. Try again.", Style.RESET_ALL)
                continue


        if guess in guessed_letters:
            print(Fore.BLUE, f"this {guess} is already guessed, please try another letters", Style.RESET_ALL)
        else:
            guessed_letters.append(guess)
            print(Fore.BLUE,f"letter added to guessed set", Style.RESET_ALL)

            # Check if the letter is in the word
            # - if so, print out to the user that they guessed correctly, add the letter to the list of correct guesses and display the updated word with the guessed letters revealed
            if guess in word_letters:
                print(Fore.GREEN, "You guessed it correctly", Style.RESET_ALL)
                correct_letters.append(guess)
                display_word(word, guessed_letters)
            else:
                # - if not, print out to the user that they guessed incorrectly and decrease the number of remaining attempts.
                # If the attempts are 0, print out to the user that they've run out of attempts, reveal the word and end the game. If the attempts are not 0, go for the next guess.

                print("Your guess was incorrect!")
                #global attempts
                attempts = attempts - 1
                print(Fore.BLUE, "lives remaining :", attempts, Style.RESET_ALL)

                print(hangman_draw[count])
                count= count+1

                if attempts == 0:
                    print(Fore.RED, "Attempts over!", Style.RESET_ALL)
                    print(Fore.RED, "You lost! here is the correct word :", word, Style.RESET_ALL)
                else:
                    print(Fore.BLUE, "you will be asked to enter inputs again...", Style.RESET_ALL)
                    continue

        # if there are no remaining letters to guess, print out to the user that they've guessed the word correctly and end the game.
        if all(letter in guessed_letters for letter in word):
            print(Fore.GREEN, "Hurray!  You Won the Game!", Style.RESET_ALL)
            print("still lives remaining :", attempts)

            #print(guessed_letters)
            #print(correct_letters)
            #print(word_letters)

            break




if __name__ == "__main__":
    hangman()
