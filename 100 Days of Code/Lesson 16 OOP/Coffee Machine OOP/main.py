# Coffee Machine Simulator using OOP
# This program simulates a coffee machine using object-oriented programming principles.
# Users can order drinks, view reports, or turn off the machine.

# Import external classes for menu, coffee maker, and money handling functionality. ***Classes were given by Udemy instructor, I just gathered evrything together to make it work 

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create object instances of the imported classes
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


# Get the available drink options as a string (e.g., "latte/espresso/cappuccino/")
options = menu.get_items()


def print_resources():
    coffee_maker.report()
    money_machine.report()


# Build a set of valid inputs (available drinks plus hidden commands)
valid = set(options.split('/')[:-1]) | {'report', 'off'}

# Prompt the user until a valid drink or command is entered
def validate_user_choice():

    while True:
        selection = input(f"What would you like? {options}:\n").strip().lower()
        if selection not in valid:
            print('Please enter one of the valid drinks available')
            continue
        else:
            break
    return selection

is_on = True 
while is_on:

    user_choice = validate_user_choice()

    # If user chooses to turn off the machine
    if user_choice == 'off':
        print('Bye!')
        break
        # If user requests a resource/money report
    elif user_choice == 'report':
        print_resources()
        # Otherwise, prepare the requested drink
    else:
        drink = menu.find_drink(user_choice)
        # If drink is not found (shouldn't happen), skip to next iteration to avoid None errors
        if drink is None:
            continue
        # Check resources and process payment before making coffee
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
    


    


