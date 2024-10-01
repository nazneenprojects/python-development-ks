"""
Alarm clock (python 3.12.5)
"""
import threading
from datetime import datetime
import time
from pyfiglet import Figlet
from colorama import init, Fore, Style
import re
#from playsound3 import playsound
import pygame

# global variables
init()
alarm_status = False
alarm_time = 0
alarm_triggered = False
pygame.mixer.init()
sound = pygame.mixer.Sound('./mixkit-retro-game-emergency-alarm-1000.wav')


def display_current_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    print("Current Time:", current_time)
    return current_time

def notify_user():
    print("\nALARM! Time to wake up!")
    input( "Press 3 from the menu to stop the alarm:")

def set_alarm():
    global alarm_status, alarm_time, alarm_triggered
    while True:
        try:
            alarm_input = input("Set the alarm time format (HH:MM): ")
            #validate_time(alarm_input)
            alarm_time = datetime.strptime(alarm_input, "%H:%M").time()
            alarm_status = True
            alarm_triggered = False

            print(f"Alarm set for {alarm_time}.")
            break
        except ValueError:
            print("Invalid time format. Please enter the time in HH:MM format.")



def validate_time(user_input: str):
    pattern = r"^(2[0-3]|[01]?[0-9])(:([0-5]?$"

    if re.match(pattern, user_input):
        print("Validation", "OK")
        #set_alarm()
    else:
        print("Validation", "Invalid Time Format")


def get_user_input():
    now = display_current_time()
    print("Current Time:", now)
    user_input = input("Please enter the time here for setting alarm  \n"
                       "(in HH:MM:SS format / 24 hours clock period) :").strip()

    if user_input:
        validate_time(user_input)
    else:
        print("somthing went wrong, try again")






def check_alarm():
    global alarm_status, alarm_triggered
    while True:
        if alarm_status:
            now = datetime.now().time()
            if now.hour == alarm_time.hour and now.minute == alarm_time.minute and not alarm_triggered:

                notify_user()
                sound.play(-1)
                alarm_triggered = True
        time.sleep(1)


def adjust_alarm():
    global alarm_time
    if alarm_status:
        while True:
            try:
                new_alarm_input = input("Enter the new alarm time (HH:MM): ")
                alarm_time = datetime.strptime(new_alarm_input, "%H:%M").time()
                print(f"Alarm adjusted to {alarm_time}.")
                break
            except ValueError:
                print("Invalid time format. Please enter the time in HH:MM format.")
    else:
        print("No active alarm to adjust.")


def stop_alarm():
    global alarm_status, alarm_triggered
    if alarm_status:
        alarm_status = False
        alarm_triggered = False
        sound.stop()
        print("Alarm stopped.")
    else:
        print("No active alarm to stop.")


def display_alarm_clock_info():
    alarm_clock_info = """
    ------------------Welcome to Alarm Clock App----------------
            Alarm Clock Menu
           
           Press 1 : Set Alarm
           Press 2: Check Alarm
           Press 3: Stop Alarm
           Press 4: Adjust Alarm
           Press 5: Exit
              
    -----------------------------------------------------------

    """

    figlet = Figlet(font='slant')
    text_art = figlet.renderText('Alarm Clock')
    print("\t \t \t", text_art)
    print("\t \t \t \t Current Time :", Fore.BLUE, datetime.now().strftime("%H:%M:%S"), Style.RESET_ALL)
    print(Fore.BLUE, "\t\t", alarm_clock_info, Style.RESET_ALL)

def alarm_clock():
    """Main alarm clock function."""

    while True:
        display_alarm_clock_info()
        choice = input("Enter your choice: ").strip()


        if choice == '1':
            set_alarm()
        elif choice == '2':
            if alarm_status:
                print(f"Alarm is set for {alarm_time}.")
            else:
                print("No alarm is set.")
        elif choice == '3':
            stop_alarm()
        elif choice == '4':
            adjust_alarm()
        elif choice == '5':
            print("Exiting Alarm Clock.")
            break
        else:
            print("Invalid choice. Please try again.")

def alarm_clock_thread():
    alarm_thread = threading.Thread(target=check_alarm)
    alarm_thread.daemon = True
    alarm_thread.start()

if __name__ == "__main__":
    alarm_clock_thread()
    alarm_clock()