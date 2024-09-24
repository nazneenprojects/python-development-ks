"""
 Simple Calculator
 This is  simple Calculator program  implemented using python 3.12.5
 This allows user to enter number and choice of operation from addition, subtraction, multiplication , division.
"""

from colorama import init, Fore, Style

init()


def start_calculator():
    """displays introductory information about this calculator program"""
    calculator_info = """
    .............................Welcome to command line simple Calculator!.......................................
    
    This Calculator program  allows you to perform operations like addition, subtraction, multiplication , division.
    You will be prompted to enter input numbers and choice of operation.
    
                                        Ready??
    ...............................................................................................................
    """
    print(Fore.BLUE, calculator_info, Style.RESET_ALL)
    input("press ENTER to continue :")
    return None


def take_input_numbers():
    """Takes operands from the user and converts them into a list by validating and converting their type to float."""
    print("Great! Now you will be prompted to enter two numbers (operands) on which you wish to perform calculations.")

    operands = []

    while len(operands) < 2:
        operand = input("Enter a number (or 'done' to finish): ").strip()

        if operand.lower() == 'done':
            if len(operands) < 2:
                print("You must enter at least two numbers before finishing.")
                continue
            break

        if not operand:
            print("Empty input is not allowed. Please enter a number.")
            continue
        elif not operand.replace('.', '', 1).isdigit():
            print("Invalid input! Please enter numeric values (no letters or special characters).")
            continue
        elif operand.count('.') > 1:
            print("Invalid input! Please enter a valid floating-point number.")
            continue

        operands.append(float(operand))

    return operands


def take_input_choice():
    """ shows options to enter a choice , to choose different operations for calculator"""
    operations_choice = """
     ......................................................
     Please enter your choice to perform below operations:
    .......................................................
     Press  1   for     ADDITION
     Press  2   for     SUBTRACTION
     Press  3   for     MULTIPLICATION
     Press  4   for     DIVISION
     Press  0   for     EXIT
     Press  r   for     RESET
     .......................................................
    """
    print(Fore.GREEN, operations_choice, Style.RESET_ALL)
    choice = input("enter your choice  :")
    return choice


def addition(operands):
    """Performs addition on the operand list

    Parameters
    ----------
    operands : [float]
        list of operands to perform addition


    Returns
    -------
    result : float
        returns float result by rounding off big result to only upto 5 decimal places
    """
    result = sum(operands)
    return round(result, 5)


def subtraction(operands):
    """Perform subtraction on operand list

    Parameters
    ----------
    operands : [float]
        list of operands to perform subtraction
        

    Returns
    -------
    result : float
        returns float result by rounding off big result to only upto 5 decimal places
    """
    result = operands[0]
    for item in operands[1:]:
        result -= item
    return round(result, 5)


def multiplication(operands):
    """Perform multiplication on the operand list

    Parameters
    ----------
    operands : [float]
        list of operands to perform multiplication
        

    Returns
    -------
    result : float
        returns float result by rounding off big result to only upto 5 decimal places
    """
    result = operands[0]
    for item in operands[1:]:
        result *= item
    return round(result, 5)


def division(operands):
    """perform division on the operand list

    Parameters
    ----------
    operands : [float]
        list of operands to perform division
        

    Returns
    -------
    result : float
        returns float result by rounding off big result to only upto 5 decimal places

    """
    result = operands[0]
    for item in operands[1:]:
        if item == 0:
            return "div by zero error"
        result /= item
    return round(result, 5)


def calculator():
    """ calculator definition call internal required function such as start_calculator() ,take_input_numbers(), take_input_choice and different operation methods """
    start_calculator()

    operands = take_input_numbers()

    while True:
        match take_input_choice():
            case '1':
                print(f"Result of Addition :  {addition(operands)}")
            case '2':
                print(f"Result of Subtraction :  {subtraction(operands)}")
            case '3':
                print(f"Result of Multiplication :  {multiplication(operands)}")
            case '4':
                print(f"Result of Division :  {division(operands)}")
            case '0':
                print("You chose to exit, goodbye!")
                break
            case 'r':
                calculator()
            case _:
                print("You entered invalid choice! resetting...")
                return "invalid operation"


if __name__ == "__main__":
    calculator()
