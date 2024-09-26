# python-development-ks
This python-development-ks repository contains projects built as a part of internship training program using python3

## Task 3: A Tip calculator

### Main Goals:
Create a program that calculates the tip amount and total bill based on user input.
Practice working with user input, variables, and basic arithmetic operations.
Implement input validation to ensure proper data entry.
Use functions to organize code and improve readability.
Format output to display currency values correctly.
Define constant of default tip percentage (set to 15%).

### Prerequisites:
- Python 3.12.5
- install pip packages using requirements.text using command  'pip install -r requirements.txt'

- pip packages used : [pyment](https://pypi.org/project/pyment/) and [colorama](https://pypi.org/project/colorama/)
- Note : how to generate automated docstring template ? 'pyment -w -o numpydoc <finename.py>'

### How to run?
python3 /a_tip_calculator/restaurant_billing/main.py

### Output
...............................................................................................................
                        Welcome to FineDine Restaurant Billing Service

        First, you will be asked to enter order items with their price.
        Based on the input, we will calculate the tip amount and total bill (including tip).
        We will print the bill for you!

        If you want to stop entering items, type 'done'. 
        Welcome again!
        ...............................................................................................................            
        
 	 	 Department Owner: Nazneen Mulani
	 	........................................................................................................
Enter the name of the food item (or type 'done' to finish and 'q' for exit from program): falafal
Enter the price for falafal: 12.89
Enter the name of the food item (or type 'done' to finish and 'q' for exit from program): hamburger
Enter the price for hamburger: 10.0
Enter the name of the food item (or type 'done' to finish and 'q' for exit from program): su§si
Invalid input. Item name should not be special char.
Enter the name of the food item (or type 'done' to finish and 'q' for exit from program): sush66
Enter the price for sush66: 12.90
Enter the name of the food item (or type 'done' to finish and 'q' for exit from program): 65chicken
Enter the price for 65chicken: 12..
Invalid price input. Please enter a valid number.
Enter the name of the food item (or type 'done' to finish and 'q' for exit from program): 54
Invalid input. Item name should not be a number.
Enter the name of the food item (or type 'done' to finish and 'q' for exit from program): chicken 65
Invalid input. Item name should not be special char.
Enter the name of the food item (or type 'done' to finish and 'q' for exit from program): chicken65
Enter the price for chicken65: 12.90
Enter the name of the food item (or type 'done' to finish and 'q' for exit from program): done
		 	...............Your Bill at FineDine Restaurant...........
		  SUBTOTAL :  48,69 €
		  TIP :  7,30 €
		  TOTAL BILL :  55,99 €
		 	..........................................................
