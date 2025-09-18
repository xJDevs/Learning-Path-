import art
import os 
'''
Auxiliar functions. Made to keep the code modular and cleaner. 
That way, all of the these lines don't need to be inside the main function. 
'''
def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    return

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b


def calculation(a, b, math_sign):

    '''
    Instead of using a bunch of if/elifs, it is better to instance a dictionary.
    Cleaner and more effective. 
    '''
    math_operations = {
        '+': addition,
        '-': subtraction,
        '*': multiplication,
        '/': division
    }
    return math_operations[math_sign](a,b)


'''
Main function. Will perform basic mathematical operations based on the inputs the user gives
'''
valid_operators = ('+', '-', '*', '/')
def calculator():

    clean_screen()
    print(f"{art.logo}\nWelcome to Joe's calculator!\n")

    while True:
        # Number1 tries to be converted to float 
        try:
            n1 = float(input('Enter your first number:\n'))
            break
        except ValueError:
            print('Please enter numbers only. They can be integers or decimals')
            continue

    should_continue = True
    while should_continue:

        # Number2 tries to be converted to float 
        try:
            n2 = float(input('What is the next number?:\n'))
        except ValueError:
            print('Please enter numbers only. They can be integers or decimals')
            continue
        
        while True:

            for sign in valid_operators:   # Would be easier to just print the operators, but for practice purposes, I use a for loop to combine different structures and force me to think a little more. 
                print(sign)
            operator = input('Select the type of math operation you want to perform:\n').strip()
            if operator not in valid_operators:
                print('Please enter a valid operator')
                continue
            else:
                break 

        if n2 == 0 and operator == '/':
                print(f'{n1} {operator} {n2} is an invalid operation')
                continue

        result = calculation(n1, n2, operator)
        
        print(f'{n1} {operator} {n2} equals {round(result, 2)}')
        another_operation = input(f"Type 'Yes' to continue calculating with {result}, 'No' to start a new calculation, or Exit to finish the program\n").strip().capitalize()
        
        if another_operation == 'Yes':
            n1 = result # The last result is stored then as n1 to continue calculating towards that
            continue
        elif another_operation == 'No':
            calculator() 
            return 
            # Here I use recursion to restart the calculator when the user chooses "No".
            # In practice, an external loop would be more efficient and scalable 
            # (avoids stack growth and potential RecursionError).
            # For learning purposes, recursion is kept to illustrate the concept.
        else:
            clean_screen()
            print("Thank you for using Joe's calculator!")
            break

calculator()





