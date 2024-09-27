"""
            Number Guessing Game [using python 3.12.5]
In this game computer guess any random number between 1 and 100 .
Then user will be given change to guess it by entering a guess one at a time to check if ,
guess matches to what computer guessed initially.
when guess matches, computer displays all the past guesses and result.
Ask if user want to continue or exit from game!
"""
import random
import sys
from colorama import init, Fore, Style

guess_list = []


def game_introduction():
    """Number Guess Game Introduction
    :return: Text output to show game information!

    Parameters
    ----------

    Returns
    -------
    Welcome message about the game
    """
    game_info = """
                        # Number Guessing Game #
    ..............................................................................................................  
    Welcome to the Game!                  
    In this, computer will guess any random number between 1 and 100 .
    Then you will be given chance to guess it by entering a guess one at a time to check if , \
    guess matches to what 
    computer guessed initially.
    when guess matches, computer displays all the past guesses and result. \
    Ask if you want to continue or exit from game!
    Ready???
    ................................................................................................................
    """
    return print(Fore.BLUE,game_info, Style.RESET_ALL)


def random_guess():
    """  Gives machine generated random number"""
    num = random.randint(1, 100)
    return num


def user_guess():
    """ takes input from user as a guess """
    num = input("Please enter the number of your own choice between 1 to 100 only:")
    return validation_of_userinput(num)


def validation_of_userinput(number):
    """Validates the user guess and only accepts int number between 0 and 100

    Parameters
    ----------
    number : user input as string form
        

    Returns
    -------
    Return the valid user input by accepting only int number between 1 and 100.
    While in other cases gives error message
    to user and also gives next chance to correct the input
    """
    try:
        while True:
            number = number.strip()
            if not number:
                print(Fore.RED, "you entered nothing, try again...", Style.RESET_ALL)
                number = input("Please enter a valid input: ")
            elif number.isalpha():
                print(Fore.RED, "invalid input, only numbers are allowed. please try again ", Style.RESET_ALL)
                number = input("Please enter a valid input: ")
            elif number.isdigit():
                number = int(number)
                if (number > 100) or (number < 0):
                    print(Fore.RED, "You entered out of range number!, pleas try again", Style.RESET_ALL)
                    number = input("Please enter a valid number between 0 and 100: ")
                else:
                    return number
            else:
                print(Fore.RED, "invalid input,only numbers are allowed. try again...", Style.RESET_ALL)
                number = input("Please enter a valid input: ")

    except ValueError:
        return "somthing went wrong, please start the game again..."


def check_choice():
    """Message for user after winning the game
    
    :return: prints the message to user after finishing game, if user wants to reset game or want to continue...

    Parameters
    ----------

    Returns
    -------
    After finishing game, this gives message to user either to continue or exit
    """
    choice_message = """
    Pleas note : 
        if you wish to reset game,   Press r
        if you wish to exit game,    Press e
    """
    print(Fore.LIGHTGREEN_EX, choice_message, Style.RESET_ALL)
    choice = input("Enter your choice :): ")

    match choice.strip():
        case 'r':
            number_guess_game()
        case 'e':
            print(Fore.RED, "you choose to exit, goodbye...", Style.RESET_ALL)
            sys.exit()
        case _:
            print(Fore.RED, "You entered invalid input! exiting...", Style.RESET_ALL)
            return "invalid operation"


def number_guess_game():
    """ This has all required functions to run the game and based on input checks if user is guessing correct number
    which was guessed by computer initially"""
    game_introduction()

    x = random_guess()
    # print("Computer Guess:", x)
    n = 0

    while x != n:
        n = user_guess()
        guess_list.append(n)
        # IMPROVE: replace the match with if-else
        # DISCUSS:
        match x:
            case _ if (x == n):
                print(Fore.BLUE, "You guessed it correctly! Hurray!", Style.RESET_ALL)
                print("Here are your guess attempts to reach here:", *guess_list, sep=', ')
                check_choice()
            case _ if (x > n):
                print("Your guess too low!")
            case _ if (x < n):
                print("your guess is too high!")


if __name__ == "__main__":
    number_guess_game()
