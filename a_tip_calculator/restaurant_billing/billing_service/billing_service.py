"""
This is billing service for:
    -   get order item price list
    -   apply tip amount
    -   calculate total bill
    -   print bill
"""
import sys
import locale
from a_tip_calculator.restaurant_billing.restaurant.restaurant import Restaurant
from colorama import init, Fore, Style

init()


class BillingService(Restaurant):
    TIP_PERCENTAGE = 0.15

    def __init__(self):
        self.amount = 0.0
        self.total_bill = 0.0
        self.tip = 0.0
        self.order_items = {}
        self.owner = "Nazneen Mulani"
        locale.setlocale(locale.LC_ALL, '')

    def billing_service(self):
        dept_info = """
        ...............................................................................................................
                        Welcome to FineDine Restaurant Billing Service

        First, you will be asked to enter order items with their price.
        Based on the input, we will calculate the tip amount and total bill (including tip).
        We will print the bill for you!

        If you want to stop entering items, type 'done'. 
        Welcome again!
        ...............................................................................................................            
        """
        print(dept_info + "\n \t \t Department Owner: " + self.owner)
        print("\t \t........................................................................................................")
        self.get_order_items()

    def get_order_items(self):
        """
        Collects item names and prices, and stores them in the order_items dictionary.
        Allows the user to finalize the order by typing 'done'.
        """
        while True:
            item_name = input(
                "Enter the name of the food item (or type 'done' to finish and 'q' for exit from program): ").strip()

            if item_name.lower() == 'done':
                self.calculate_bill()
                return
            elif not item_name:
                print("You entered nothing. Please provide a valid item name.")
                continue
            elif item_name.isdigit():
                print("Invalid input. Item name should not be a number.")
                continue
            elif item_name.strip().lower() == "q":
                raise SystemError

            try:
                item_price = float(input(f"Enter the price for {item_name}: ").strip())
                if item_price < 0:
                    print("Price should be a positive number.")
                    continue

            except ValueError:
                print("Invalid price input. Please enter a valid number.")
                continue

            self.order_items[item_name] = item_price

    def calculate_bill(self):
        """
        Calculate total bill including tip, based on the items entered.
        """
        amount = sum(self.order_items.values())
        self.total_bill = self.calculate_total_bill(amount)
        # self.print_bill()

    def apply_tip_amount(self, amount):
        """
        Applies a tip percentage to the amount.
        """
        return amount * self.TIP_PERCENTAGE

    def calculate_total_bill(self, amount):
        """
        Calculates the total bill including the tip.
        """
        self.tip = self.apply_tip_amount(amount)
        total_bill = amount + self.tip
        self.print_bill(self.tip, amount, total_bill)
        return total_bill

    def print_bill(self, tip: float, amount: float, total_bill: float):
        """
        Prints the final bill including total amount in local currency .
        """
        subtotal = locale.currency(amount, grouping=True, international=False)
        tip = locale.currency(tip, grouping=True, international=False)
        bill = locale.currency(total_bill, grouping=True, international=False)

        print("\t\t \t...............Your Bill at FineDine Restaurant...........")
        print("SUBTOTAL : ", subtotal)
        print("TIP : ", tip)
        print("TOTAL BILL : ", bill)
        print("\t\t \t..........................................................")
