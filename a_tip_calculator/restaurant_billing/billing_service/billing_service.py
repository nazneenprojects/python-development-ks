"""
This is billing service for:
    -   get order item price list
    -   apply tip amount
    -   calculate total bill
    -   print bill
"""
import sys

from a_tip_calculator.restaurant_billing.restaurant.restaurant import Restaurant
from colorama import init, Fore, Style

init()
total_bill = 0  # global variable for total bill
order_items = {}  # global variable for taking order items from user


class BillingService(Restaurant):
    TIP_PERCENTAGE = 15

    def __init__(self):
        #super().__init__()
        self.amount = 0.0
        self.owner = "Nazneen Mulani"

    def validate_user_input_name(self, input):
        pass

    def validate_user_input_price(self, input):
        pass

    def billing_service(self):
        dept_info = """
        ...............................................................................................................
                        Welcome to FineDine Restaurant Billing Service
        
        First you wil be asked to enter order item with price. 
        Bsed on input , we will calculate tip amount and total bill (including tip)
        We will print bill for you!
        
        If you want to stop and exit in between please press     'e' 
        Welcome again!
        ...............................................................................................................            
        """
        print(dept_info + "\n \t \t Department Owner:" + self.owner)
        self.calculate_bill()


    # def check_choice(self):
    #     """Message for user printing bill of current order
    #
    #     :return: prints the message to user after finishing calci, if user wants to reset  or want to exit...
    #
    #     Parameters
    #     ----------
    #
    #     Returns
    #     -------
    #     After finishing game, this gives message to user either to continue or exit
    #     """
    #     choice_message = """
    #     Pleas note :
    #         if you wish to reset game,   Press r
    #         if you wish to exit game,    Press e
    #     """
    #     print(Fore.LIGHTGREEN_EX, choice_message, Style.RESET_ALL)
    #     choice = input("Enter your choice :): ")
    #
    #     match choice.strip():
    #         case 'r':
    #             self.calculate_bill()
    #         case 'e':
    #             print(Fore.RED, "you choose to exit, goodbye...", Style.RESET_ALL)
    #             sys.exit()
    #         case _:
    #             print(Fore.RED, "You entered invalid input! exiting...", Style.RESET_ALL)
    #             return "invalid operation"

    def calculate_bill(self):
        global order_items
        try:
            while True:
                item_name = input("Enter your name of the food order   : ")
                self.validate_user_input_name(item_name)

                item_price = input("Enter the price of the same food item which you entered above     :")
                self.validate_user_input_price(item_price)

                order_items[item_name] = item_price

                more_items = input("do you wan to add more items? (yes/no):").strip().lower()
                if more_items != "yes":
                    break

                # print("\n Order Items and their prices:")
                # for item_name, item_price in order_items.items():
                #     print(f"{item_name}: ${item_price:.2f}")

                # ---------------fix this part -----------------
                total = sum(int(order_items.values()))
                global total_bill
                total_bill = self.calculate_total_bill(int(total))
                return  self.print_bill(total_bill)

        except ValueError:
            return "somthing went wrong, please start the game again..."

    @staticmethod
    def apply_tip_amount(amount):
        tip_percentage = BillingService.TIP_PERCENTAGE
        return amount * (tip_percentage / 100)

    def calculate_total_bill(self, amount):
        tip = self.apply_tip_amount(amount)
        global total_bill
        total_bill = self.amount + tip
        return total_bill

    @staticmethod
    def print_bill(total_amount):
        print_copy = "Thank you for your visit! Your total bill is: ", {total_amount}
        return print_copy
