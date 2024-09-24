"""
            Number Guessing Game [using python 3.12.5]
In this game computer guess any random number between 1 and 100 .
Then user will be given change to guess it by entering a guess one at a time to check if , guess matches to what computer guessed initially.
when guess matches, computer displays all the past guesses and result. Ask if user want to continue or exit from game!
"""
import random

guess_list = []


def game_introduction():
    """ Number Guess Game Introduction
    :return: Text output to show game information!
    """
    game_info = """
                        # Number Guessing Game #
    ..............................................................................................................  
    Welcome to the Game!                  
    In this, computer will guess any random number between 1 and 100 .
    Then you will be given chance to guess it by entering a guess one at a time to check if , guess matches to what 
    computer guessed initially.
    when guess matches, computer displays all the past guesses and result. Ask if you want to continue or exit from game!
    Read???
    ................................................................................................................
    """
    return print(game_info)


def random_guess():
    num = random.randint(1, 100)
    return num


def user_guess():
    num = input("Please enter the number of your own choice between 1 to 100 only:")
    # validation_of_userinput(num)
    return validation_of_userinput(num)


def validation_of_userinput(number: int):
    number = int(number)
    return number


def check_choice():
    """Message for user after winning the game

    :return: prints the message to user after finishing game, if user wants to reset game or want to continue...
    """
    choice_message = """
    Pleas note : 
        if you wish to reset game in between,   Press r
        if you wish to exit game in between,    Press e
    """
    print(choice_message)
    user_command = input("Enter your choice :): ")

    match user_command:
        case 'r':
            number_guess_game()
        case 'e':
            print("you choose to exit, goodbye...")
            pass
        case _:
            print("You entered invalid input! exiting...")
            return "invalid operation"


def number_guess_game():
    game_introduction()

    x = random_guess()
    # print("Computer Guess:", x)
    n = 0

    while x != n:
        n = user_guess()
        guess_list.append(n)
        match x:
            case _ if (x == n):
                print("You guessed it correctly! Hurray!")
                print("Here are your guess attempts to reach here:", *guess_list, sep=', ')
                check_choice()
            case _ if (x > n):
                print("Your guess too low!")
            case _ if (x < n):
                print("your guess is too high!")


if __name__ == "__main__":
    number_guess_game()
