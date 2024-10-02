# python-development-ks
This python-development-ks repository contains projects built as a part of internship training program using python3

## Task 7: Hangman Game
Hangman Game [using python 3.12.5]
Choose a word: The game randomly selects a word from a predefined list of words.
Display blanks: Display a series of dashes, representing each letter of the word to be guessed.
Guess a letter: Prompt the player to guess a letter. Validate the input (if it is not a single letter, or if it isn’t a letter.)
Check the guess: Check if the guessed letter is in the word. If it is, reveal the letter in its correct position(s) in the blanks. If not, decrease the number of remaining attempts.
Repeat: Repeat steps 3-4 until the player either guesses the word correctly or runs out of attempts.
End game: If the player guesses the word correctly within the allowed attempts, congratulate them. Otherwise, reveal the word and inform them that they have lost.

### Main Goals:
- Computer will choose random word
- You have to guess it key entering single letter at a time

### Prerequisites:
- Python 3.12.5
- install pip packages using requirements.text using command  'pip install -r requirements.txt'

- 

### How to run?
    ```python3 hangman_game.py

### Output

Round 1:

                
                 +---+
          |   |
              |
              |
              |
              |
        =========
                         __  __                                            ______                   
           / / / /___ _____  ____ _____ ___  ____ _____      / ____/___ _____ ___  ___ 
          / /_/ / __ `/ __ \/ __ `/ __ `__ \/ __ `/ __ \    / / __/ __ `/ __ `__ \/ _ \
         / __  / /_/ / / / / /_/ / / / / / / /_/ / / / /   / /_/ / /_/ / / / / / /  __/
        /_/ /_/\__,_/_/ /_/\__, /_/ /_/ /_/\__,_/_/ /_/____\____/\__,_/_/ /_/ /_/\___/ 
                          /____/                     /_____/                           
        
        word chosen by computer: apple
        _ _ _ _ _
        Guess a letter: #
         That is not a letter. Please guess a valid letter.
        Guess a letter: 7
         That is not a letter. Please guess a valid letter.
        Guess a letter: rtz
         Multiple char or word now allowed . please enter only single letter 
        Guess a letter: e
         letter added to guessed set 
         You guessed it correctly 
        _ _ _ _ e
        Guess a letter: z
         letter added to guessed set 
        Your guess was incorrect!
         lives remaining : 5 
        
          +---+
          |   |
              |
              |
              |
              |
        =========
         you will be asked to enter inputs again... 
        Guess a letter: f
         letter added to guessed set 
        Your guess was incorrect!
         lives remaining : 4 
        
          +---+
          |   |
          O   |
              |
              |
              |
        =========
         you will be asked to enter inputs again... 
        Guess a letter: g
         letter added to guessed set 
        Your guess was incorrect!
         lives remaining : 3 
        
          +---+
          |   |
          O   |
          |   |
              |
              |
        =========
         you will be asked to enter inputs again... 
        Guess a letter: h
         letter added to guessed set 
        Your guess was incorrect!
         lives remaining : 2 
        
          +---+
          |   |
          O   |
         /|   |
              |
              |
        =========
         you will be asked to enter inputs again... 
        Guess a letter: c
         letter added to guessed set 
        Your guess was incorrect!
         lives remaining : 1 
        
          +---+
          |   |
          O   |
         /|\  |
              |
              |
        =========
         you will be asked to enter inputs again... 
        Guess a letter: q
         letter added to guessed set 
        Your guess was incorrect!
         lives remaining : 0 
        
          +---+
          |   |
          O   |
         /|\  |
         /    |
              |
        =========
         Attempts over! 
         You lost! here is the correct word : apple 


Round 2 :



![Screenshot from 2024-10-02 12-50-07.png](Screenshot%20from%202024-10-02%2012-50-07.png)
![Screenshot from 2024-10-02 12-50-57.png](Screenshot%20from%202024-10-02%2012-50-57.png)
![Screenshot from 2024-10-02 12-51-40.png](Screenshot%20from%202024-10-02%2012-51-40.png)
