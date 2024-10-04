# python-development-ks
This python-development-ks repository contains projects built as a part of internship training program using python3

## Task 8: Hangman Game
Delivery Fee Calculator [using python 3.12.5]


### Main Goals:
Your task is to write a delivery fee calculator. This code is needed when a customer is ready with their shopping cart and we’d like to show them how much the delivery will cost. The delivery price depends on the cart value, the number of items in the cart, the time of the order, and the delivery distance.

1. Specification
Rules for calculating a delivery fee

If the cart value is less than 10€, a small order surcharge is added to the delivery price. The surcharge is the difference between the cart value and 10€. For example if the cart value is 8.90€, the surcharge will be 1.10€.
A delivery fee for the first 1000 meters (=1km) is 2€. If the delivery distance is longer than that, 1€ is added for every additional 500 meters that the courier needs to travel before reaching the destination. Even if the distance would be shorter than 500 meters, the minimum fee is always 1€.
Example 1: If the delivery distance is 1499 meters, the delivery fee is: 2€ base fee + 1€ for the additional 500 m => 3€
Example 2: If the delivery distance is 1500 meters, the delivery fee is: 2€ base fee + 1€ for the additional 500 m => 3€
Example 3: If the delivery distance is 1501 meters, the delivery fee is: 2€ base fee + 1€ for the first 500 m + 1€ for the second 500 m => 4€
If the number of items is five or more, an additional 50 cent surcharge is added for each item above and including the fifth item. An extra “bulk” fee applies for more than 12 items of 1,20€
Example 1: If the number of items is 4, no extra surcharge
Example 2: If the number of items is 5, 50 cents surcharge is added
Example 3: If the number of items is 10, 3€ surcharge (6 x 50 cents) is added
Example 4: If the number of items is 13, 5,70€ surcharge is added ((9 * 50 cents) + 1,20€)
Example 5: If the number of items is 14, 6,20€ surcharge is added ((10 * 50 cents) + 1,20€)
The delivery fee can never be more than 15€, including possible surcharges.
The delivery is free (0€) when the cart value is equal or more than 200€.
During the Friday rush, 3 - 7 PM, the delivery fee (the total fee including possible surcharges) will be multiplied by 1.2x. However, the fee still cannot be more than the max (15€). Timezone isn’t that important. The original task had the following timezone definition:
Considering timezone, for simplicity, use UTC as a timezone in backend solutions (so Friday rush is 3 - 7 PM UTC). In frontend solutions, use the timezone of the browser (so Friday rush is 3 - 7 PM in the timezone of the browser).

### Prerequisites:
- Python 3.12.5


### How to run?
    python3 delievery_fee_calci.py

### Output
    
### Test 1:
    
     ____       ___                          ______        
       / __ \___  / (_)   _____  _______  __   / ____/__  ___ 
      / / / / _ \/ / / | / / _ \/ ___/ / / /  / /_  / _ \/ _ \
     / /_/ /  __/ / /| |/ /  __/ /  / /_/ /  / __/ /  __/  __/
    /_____/\___/_/_/ |___/\___/_/   \__, /  /_/    \___/\___/ 
                                   /____/                     
       ______      __           __      __            
      / ____/___ _/ /______  __/ /___ _/ /_____  _____
     / /   / __ `/ / ___/ / / / / __ `/ __/ __ \/ ___/
    / /___/ /_/ / / /__/ /_/ / / /_/ / /_/ /_/ / /    
    \____/\__,_/_/\___/\__,_/_/\__,_/\__/\____/_/     
                                                      
    
    
            -------------------------------------------------------------------------------
            This is  delivery fee calculator App
            he delivery price depends on the cart value, the number of items in the cart, 
    
            the time of the order, and the delivery distance.
            
            
            You will be asked to enter :
            CART_VALUE (in cents)
            NUMBER OF ITEMS
            TIME OF ORDER
            DELIVERY DISTANCE
        -------------------------------------------------------------------------------
        
    Please enter Cart Value (in cents, whole number): 790
    Please enter total number of items: 4
    Please enter delivery time (YYYY-MM-DD HH:MM:SS): 2024-01-15 13:00:00
    Please enter delivery distance (in meters): 2235
    The total delivery fee in Cents is: 710 cents
    The total delivery fee in Euro is: 7,10 € 


### Test 2:

            ____       ___                          ______        
       / __ \___  / (_)   _____  _______  __   / ____/__  ___ 
      / / / / _ \/ / / | / / _ \/ ___/ / / /  / /_  / _ \/ _ \
     / /_/ /  __/ / /| |/ /  __/ /  / /_/ /  / __/ /  __/  __/
    /_____/\___/_/_/ |___/\___/_/   \__, /  /_/    \___/\___/ 
                                   /____/                     
       ______      __           __      __            
      / ____/___ _/ /______  __/ /___ _/ /_____  _____
     / /   / __ `/ / ___/ / / / / __ `/ __/ __ \/ ___/
    / /___/ /_/ / / /__/ /_/ / / /_/ / /_/ /_/ / /    
    \____/\__,_/_/\___/\__,_/_/\__,_/\__/\____/_/     
                                                      
    
    
            -------------------------------------------------------------------------------
            This is  delivery fee calculator App
            he delivery price depends on the cart value, the number of items in the cart, 
    
            the time of the order, and the delivery distance.
            
            
            You will be asked to enter :
            CART_VALUE (in cents)
            NUMBER OF ITEMS
            TIME OF ORDER
            DELIVERY DISTANCE
        -------------------------------------------------------------------------------
        
    Please enter Cart Value (in cents, whole number): 67.
    Invalid input. Please enter a valid integer value for cart value in cents.
    Please enter Cart Value (in cents, whole number): 780
    Please enter total number of items: 0
    Invalid input. Please enter a valid number of items.
    Please enter total number of items: #
    Invalid input. Please enter a valid number of items.
    Please enter total number of items: 12
    Please enter delivery time (YYYY-MM-DD HH:MM:SS): 2021-10-21T13:00:0
    Invalid time format. Please enter in the format YYYY-MM-DD HH:MM:SS.
    Please enter delivery time (YYYY-MM-DD HH:MM:SS): 2021-10-21 13:00:0
    Please enter delivery distance (in meters): 89999
    The total delivery fee in Cents is: 1500 cents



## Test 3:

            ____       ___                          ______        
       / __ \___  / (_)   _____  _______  __   / ____/__  ___ 
      / / / / _ \/ / / | / / _ \/ ___/ / / /  / /_  / _ \/ _ \
     / /_/ /  __/ / /| |/ /  __/ /  / /_/ /  / __/ /  __/  __/
    /_____/\___/_/_/ |___/\___/_/   \__, /  /_/    \___/\___/ 
                                   /____/                     
       ______      __           __      __            
      / ____/___ _/ /______  __/ /___ _/ /_____  _____
     / /   / __ `/ / ___/ / / / / __ `/ __/ __ \/ ___/
    / /___/ /_/ / / /__/ /_/ / / /_/ / /_/ /_/ / /    
    \____/\__,_/_/\___/\__,_/_/\__,_/\__/\____/_/     
                                                      
    
    
            -------------------------------------------------------------------------------
            This is  delivery fee calculator App
            he delivery price depends on the cart value, the number of items in the cart, 
    
            the time of the order, and the delivery distance.
            
            
            You will be asked to enter :
            CART_VALUE (in cents)
            NUMBER OF ITEMS
            TIME OF ORDER
            DELIVERY DISTANCE
        -------------------------------------------------------------------------------
        
    Please enter Cart Value (in cents, whole number): 2000
    Please enter total number of items: 1
    Please enter delivery time (YYYY-MM-DD HH:MM:SS): 2021-10-21 13:00:00
    Please enter delivery distance (in meters): 900
    The total delivery fee in Cents is: 200 cents
    The total delivery fee in Euro is: 2,00 € 





