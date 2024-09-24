# python-development-ks
This python-development-ks repository contains projects built as a part of internship training program using python3

## Task 2: Number Guessing Game
Number Guessing Game [using python 3.12.5]
In this game computer guess any random number between 1 and 100 .
Then user will be given change to guess it by entering a guess one at a time to check if , guess matches to what computer guessed initially.
when guess matches, computer displays all the past guesses and result. Ask if user want to continue or exit from game!

### Main Goals:
- Create a game where the computer generates a random number and the user tries to guess it.
- Implement input validation and provide feedback to the user.
- Use loops to allow multiple guesses.

### Prerequisites:
- Python 3.12.5
- install pip packages using requirements.text using command  'pip install -r requirements.txt'

- pip packages used : [pyment](https://pypi.org/project/pyment/) , [colorama](https://pypi.org/project/colorama/) , sys, random
- Note : how to generate automated docstring template ? 'pyment -w -o numpydoc <finename.py>'

### How to run?
    ```python3 number_guess_game.py

### Output
```
                        # Number Guessing Game #
    ..............................................................................................................  
    Welcome to the Game!                  
    In this, computer will guess any random number between 1 and 100 .
    Then you will be given chance to guess it by entering a guess one at a time to check if , guess matches to what 
    computer guessed initially.
    when guess matches, computer displays all the past guesses and result. Ask if you want to continue or exit from game!
    Ready???
    ................................................................................................................
    
Please enter the number of your own choice between 1 to 100 only:123
You entered out of range number!, pleas try again
Please enter a valid number between 0 and 100: 12
Your guess too low!
Please enter the number of your own choice between 1 to 100 only:50
your guess is too high!
Please enter the number of your own choice between 1 to 100 only:25
Your guess too low!
Please enter the number of your own choice between 1 to 100 only:35
Your guess too low!
Please enter the number of your own choice between 1 to 100 only:45
your guess is too high!
Please enter the number of your own choice between 1 to 100 only:40
your guess is too high!
Please enter the number of your own choice between 1 to 100 only:38
your guess is too high!
Please enter the number of your own choice between 1 to 100 only:36
You guessed it correctly! Hurray!
Here are your guess attempts to reach here:, 12, 50, 25, 35, 45, 40, 38, 36

    Pleas note : 
        if you wish to reset game,   Press r
        if you wish to exit game,    Press e
    
Enter your choice :): 