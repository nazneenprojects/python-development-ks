import math
from datetime import datetime
import locale

from pyfiglet import Figlet

# global variables
delivery_fee = 0.0
locale.setlocale(locale.LC_ALL, '')


def calculate_distance_fee(delivery_distance):
    BASE_FEE_1KM = 200  # Base fee for the first kilometer (200 cents)
    ADDITIONAL_FEE_PER_500M = 100  # Fee for each additional 500 meters (100 cents)
    BASE_DISTANCE = 1000  # Base distance in meters

    distance_fee = BASE_FEE_1KM

    if delivery_distance > BASE_DISTANCE:
        additional_distance = delivery_distance - BASE_DISTANCE
        additional_units = math.ceil(additional_distance / 500)
        distance_fee += additional_units * ADDITIONAL_FEE_PER_500M

    return distance_fee


def calculate_surcharge(number_of_items):
    SURCHARGE_ITEM_LIMIT = 5  # Number of items at which surcharge starts
    BULK_ITEM_LIMIT = 12  # Bulk item limit
    BULK_FEE = 120  # Bulk fee for more than 12 items (120 cents)
    SURCHARGE_PER_ITEM_ABOVE_FIVE = 50  # Surcharge for items above five (50 cents)

    surcharge = 0
    if number_of_items >= SURCHARGE_ITEM_LIMIT:
        surcharge += (number_of_items - SURCHARGE_ITEM_LIMIT + 1) * SURCHARGE_PER_ITEM_ABOVE_FIVE

    if number_of_items > BULK_ITEM_LIMIT:
        surcharge += BULK_FEE

    return surcharge


def calculate_cart_value_surcharge(cart_value):
    MINIMUM_CART_VALUE = 1000  # Minimum cart value in cents (10€)
    if cart_value < MINIMUM_CART_VALUE:
        return MINIMUM_CART_VALUE - cart_value  # Surcharge in cents
    return 0


def friday_rush_hours_delivery_charges(total_fee, delivery_time):
    RUSH_HOUR_RATE = 1.2
    FRIDAY = 4

    if delivery_time.weekday() == FRIDAY and 15 <= delivery_time.hour < 19:
        total_fee *= RUSH_HOUR_RATE

    return total_fee


def calculate_total_delivery_fee(cart_value: int, number_of_items: int, delivery_time: datetime,
                                 delivery_distance: float) -> int:
    MAX_DELIVERY_FEE = 1500  # Maximum delivery fee in cents (15€)
    FREE_DELIVERY_LIMIT = 20000  # Free delivery limit in cents (200€)

    if cart_value >= FREE_DELIVERY_LIMIT:
        return 0

    # Calculate surcharges
    cart_surcharge = calculate_cart_value_surcharge(cart_value)
    item_surcharge = calculate_surcharge(number_of_items)
    distance_fee = calculate_distance_fee(delivery_distance)


    total_fee = cart_surcharge + item_surcharge + distance_fee


    total_fee = friday_rush_hours_delivery_charges(total_fee, delivery_time)


    return min(total_fee, MAX_DELIVERY_FEE)


def convert_cents_to_euros(cents):
    euros = int(cents) / 100
    return euros




def get_cart_value() -> int:
    while True:
        cart_val = input("Please enter Cart Value (in cents, whole number): ").strip()
        try:
            cart_val = int(cart_val)
            if cart_val < 0:
                print("Cart value must be a non-negative integer. Try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid integer value for cart value in cents.")
            continue

        return cart_val

def get_number_of_items():
    while True:
        number_of_items = input("Please enter total number of items: ").strip()
        if not number_of_items.isdigit() or int(number_of_items) <= 0:
            print("Invalid input. Please enter a valid number of items.")
            continue
        return int(number_of_items)


def get_delivery_time():
    while True:
        delivery_time_input = input("Please enter delivery time (YYYY-MM-DD HH:MM:SS): ").strip()
        try:
            delivery_time = datetime.strptime(delivery_time_input, '%Y-%m-%d %H:%M:%S')
            return delivery_time
        except ValueError:
            print("Invalid time format. Please enter in the format YYYY-MM-DD HH:MM:SS.")


def get_delivery_distance():
    while True:
        try:
            delivery_distance = float(input("Please enter delivery distance (in meters): ").strip())
            if delivery_distance <= 0:
                print("Delivery distance must be greater than zero.")
                continue
            return delivery_distance
        except ValueError:
            print("Invalid input. Please enter a valid delivery distance in meters.")

def get_user_inputs():
    cart_value = get_cart_value()
    #cart_value_euro = convert_cents_to_euros(cart_value)
    #print("cart_value in euro:", cart_value_euro)
    number_of_items = get_number_of_items()
    delivery_time = get_delivery_time()
    delivery_distance = get_delivery_distance()
    return cart_value, number_of_items, delivery_time, delivery_distance

def delivery_fee_calculator():
    figlet = Figlet(font='slant')
    text_art = figlet.renderText('Delivery Fee Calculator')

    print(text_art)

    app_info = """
        -------------------------------------------------------------------------------
        This is  delivery fee calculator App
        he delivery price depends on the cart value, the number of items in the cart, \n
        the time of the order, and the delivery distance.
        
        
        You will be asked to enter :
        CART_VALUE (in cents)
        NUMBER OF ITEMS 
        TIME OF ORDER (in YYYY-MM-DD HH:MM:SS.)
        DELIVERY DISTANCE (in meters)
    -------------------------------------------------------------------------------
    """
    print(app_info)

    cart_value, number_of_items, delivery_time, delivery_distance = get_user_inputs()
    total_delivery_fee = calculate_total_delivery_fee(cart_value, number_of_items, delivery_time, delivery_distance)

    print(f"The total delivery fee in Cents is: {total_delivery_fee} cents")
    total_delivery_fee_euro = locale.currency(convert_cents_to_euros(total_delivery_fee), grouping=True, international=False)
    print(f"The total delivery fee in Euro is: {total_delivery_fee_euro} ")




if __name__ == '__main__':
    delivery_fee_calculator()
