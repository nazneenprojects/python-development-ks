"""
        a tip calculator [using python 3.12.5]
This is a Tip Calculator Program for Restaurants. It helps to show tip amount customer has to pay on te bill
Note - default tip percentage (set to 15%)
"""
from a_tip_calculator.restaurant_billing.billing_service.billing_service import BillingService

if __name__ == "__main__":

    bill = BillingService()
    bill.billing_service()





