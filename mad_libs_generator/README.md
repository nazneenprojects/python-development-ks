# python-development-ks
This python-development-ks repository contains projects built as a part of internship training program using python3

## Task 4: Mad libs Generator
Mad lab generator [using python 3.12.5]


### Main Goals:
- Create a program that generates a story by asking the user for various words.
- Use string formatting to insert the user’s words into a pre-written story.
- Implement functions to make the code more organized.
- get user input for different types of words (nouns, verbs, adjectives, etc.).
- Allow the user to generate multiple stories or exit the program.

### Prerequisites:
- Python 3.12.5

### How to run?
    ```python3 mad_libs_generator.py

### future scope
- handle more specific  cases validation

### output

        I will help you to write a story. you will be asked to enter some words (noun or verbs or adjectives).
                                  Please select the topic from below gen option 
                                  ----------------------------------------------------------
                                  PRESS 1       for Rain Day
                                  PRESS 2       for Visiting China
                                  PRESS 3       for It's about Coffeehouse
                                  PRESS r       reset
                                  PRESS q       exit

                                  ----------------------------------------------------------

                                  
Enter your choice :1
take inputs ..
Enter the noun1 :Reno
Enter the noun2 :Chris
Enter the noun3 :Tom
Enter the adj :carefully
Enter the verb :running
Thank you, you entered below words :
noun1: Reno
noun2: Chris
noun3: Tom
adj: carefully
verb: running

    One day, I was walking my Reno , when Chris 
    started from the sky! I called my friend Tom 
    and she said one just landed right on her carefully! 
    There was raining stretch as well and they were just running everywhere! 
    
------------------story creation completed-------------------

 I will help you to write a story. you will be asked to enter some words (noun or verbs or adjectives).
                                  Please select the topic from below gen option 
                                  ----------------------------------------------------------
                                  PRESS 1       for Rain Day
                                  PRESS 2       for Visiting China
                                  PRESS 3       for It's about Coffeehouse
                                  PRESS r       reset
                                  PRESS q       exit

                                  ----------------------------------------------------------

                                  
Enter your choice :2
take inputs ..
Enter the noun1 :zuki
Enter the noun2 :olaf
Enter the noun3 :wer#
Traceback (most recent call last):
  File "/home/zermatt/Documents/python-development-ks/mad_libs_generator/mad_libs_generator.py", line 117, in <module>
    mad_lib_generator()
  File "/home/zermatt/Documents/python-development-ks/mad_libs_generator/mad_libs_generator.py", line 102, in mad_lib_generator
    story_visiting_china(get_user_inputs())
                         ^^^^^^^^^^^^^^^^^
  File "/home/zermatt/Documents/python-development-ks/mad_libs_generator/mad_libs_generator.py", line 30, in get_user_inputs
    raise  ValueError
ValueError