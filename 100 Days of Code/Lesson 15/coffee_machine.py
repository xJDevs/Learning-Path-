import menu
MENU = menu.MENU
resources = menu.resources
profit = 0

def process_coins():
    '''Will ask the user to insert coins. The function will calculate the amount of money entered by the user '''
    print('Please insert coins')

    while True:

        quarters = input('How many quarters?: ').strip() 
        dimes = input('How many dimes?: ').strip() 
        nickels = input('How many nickels?: ').strip() 
        pennies = input('How many pennies?: ').strip()

        try: 
            quarters = int(quarters) 
            dimes = int(dimes) 
            nickels = int(nickels) 
            pennies = int(pennies) 
            break
        except ValueError:
            print('Please enter numbers only')
            continue
    
    total = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)

    return round(total, 2)

def ask_user():
    '''Will prompt the user to select one the coffee options available
    Will also contain certain secret function: report and off 
    '''
    while True:
            
        user_choice = input("What would you like to order?\n"
                            f"1. Espresso ${MENU['espresso']['cost']:.2f}\n"
                            f"2. Latte ${MENU['latte']['cost']:.2f}\n"
                            f"3. Cappuccino ${MENU['cappuccino']['cost']:.2f}\n>"
                            ).lower().strip()

        if user_choice == 'report':
            print(f"Water: {resources['water']} ml\n"
                  f"Milk: {resources['milk']} ml\n"
                  f"Coffee: {resources['coffee']} g\n"
                  f"Money: ${profit:.2f}\n")
            continue
        elif user_choice == 'off':
            print('Turning Off CoffeeMachine...')
            return 
        else:
            if user_choice not in ('1','2','3'):
                print("Please select one of the valid options: 1, 2 or 3")
                continue
            else:
                return user_choice
        
    
def check_resources(drink):
    '''Will compare that the ingredients required for the drink selected, 
    are available in the resources contained in the machine
    With just one ingredient missing, returns False 
    '''
    for ingredient in drink:
        if resources[ingredient] < drink[ingredient]:
            print(f'Sorry there is not enough {ingredient}\n')
            return False 
    return True 

options = {
    '1': 'espresso',
    '2': 'latte',
    '3': 'cappuccino'
}

def coffee_machine():

    global profit 

    while True:
        user_selection = ask_user() 

        if user_selection is None:
            break 

        coffee_name = options[user_selection]
        drink_selected = MENU[coffee_name]
        ingredients = drink_selected['ingredients']
        cost = drink_selected['cost']

        resources_available = check_resources(ingredients)

        if not resources_available:
            continue
        else:
            money = process_coins()

            if money >= cost:
                change = round(money - cost)
                profit += cost
                for ingredient, amount in drink_selected['ingredients'].items():
                    resources[ingredient] -= amount
            else:
                print(f"Sorry that's not enough money. Money refunded: ${money:.2f}\n")
                continue

        print(f'Here is your change {change:.2f}\nHere is your {coffee_name} ☕️. Enjoy!\n')


    
coffee_machine()
