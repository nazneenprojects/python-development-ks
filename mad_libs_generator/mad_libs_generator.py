"""
This is Mad Lib Generator to create custom stories
"""

user_words = {
    "noun1": "[word_not_entered]",
    "noun2": "[word_not_entered]",
    "noun3": "[word_not_entered]",
    "adj": "[word_not_entered]",
    "verb": "[word_not_entered]",
}


def check_validation(word: str) -> bool:
    pass


def get_user_inputs():
    global user_words
    print("take inputs ..")
    for k in user_words:
        temp = input(f"Enter the {k} :").strip()
        if temp.isalpha():
            user_words[k] = temp
        else:
            raise ValueError

    print("Thank you, you entered below words :")
    for key, value in user_words.items():
        print(f"{key}: {value}")
    return user_words


def story_rainy_day(inputs: dict):
    story_template = """
    One day, I was walking my {noun1} , when {noun2} 
    started from the sky! I called my friend {noun3} 
    and she said one just landed right on her {adj}! 
    There was raining stretch as well and they were just {verb} everywhere! 
    """

    print(story_template.format(**inputs))
    return


def story_visiting_china(inputs: dict):
    story_template = """
    When {noun1}
    was {adj}
    , her parents told her they were going on a trip to China. They told her to pack her {noun2}
    . The plane ride was {verb}
    hours long! She {verb}
    and {noun3}
    . When they got to China, she was very young
    """
    print(story_template.format(**inputs))
    return


def stroy_coffeehouse(inputs: dict):
    story_template = """
    When {noun1}
    was {adj}
    , her parents told her they were going on a trip to Coffeehouse. They told her to pack her {noun2}
    . The plane ride was {verb}
    hours long! She {verb}
    and {noun3}
    . When they got to China, she was very tired
    """
    print(story_template.format(**inputs))
    return


def mad_lib_generator():
    while True:

        print(""" I will help you to write a story. you will be asked to enter some words (noun or verbs or adjectives).
                                  Please select the topic from below gen option 
                                  ----------------------------------------------------------
                                  PRESS 1       for Rain Day
                                  PRESS 2       for Visiting China
                                  PRESS 3       for It's about Coffeehouse
                                  PRESS r       reset
                                  PRESS q       exit

                                  ----------------------------------------------------------

                                  """)
        # inputs = get_user_inputs()
        story_choice = input("Enter your choice :")

        match story_choice:
            case '1':
                story_rainy_day(get_user_inputs())
                print("------------------story creation completed-------------------")
            case '2':
                story_visiting_china(get_user_inputs())
            case '3':
                stroy_coffeehouse(get_user_inputs())
            case 'r':
                print("you choose to reset")
                mad_lib_generator()
            case 'q':
                print("you choose to exit, goodbye")
                break
            case '_':
                print("invalid input, resetting ")
                mad_lib_generator()


if __name__ == "__main__":
    mad_lib_generator()
