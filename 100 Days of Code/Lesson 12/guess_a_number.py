import random

'''Creates the list from 1 to 100 and picks a randm number from that list'''
numbers = []
for number in range(1, 101):
    numbers.append(number)
secret_number = random.choice(numbers)

'''Difficulties are instanced on a dictionary for easy access'''
attempts_per_difficulty = {
    'easy': 10,
    'hard': 5
}

'''
This will retrun the amount of attempts from the dictionary based on the user selection.
Validates also user can only enter 'easy' or 'hard' word 
'''
def difficulty_selection():

    while True:
        diff_selection = input("Choose a difficulty. Type 'Easy' or 'Hard':\n").lower().capitalize()
        if diff_selection == 'Easy':
            return attempts_per_difficulty['easy']
        elif diff_selection == 'Hard':   
            return attempts_per_difficulty['hard']
        else:
            print('Please choose a valid difficulty')
            continue


'''
Asks user for a guess
Validates it is between 1 and 100
Validates it accepts numbers only 
'''
def make_guess():

    while True:
        try:
            guess = int(input('Make a guess: '))
            if guess < 1 or guess > 100:
                print('Your guess must be between 1 and 100')
                continue
            else:
                break 
        except ValueError:
            print('Please enter numbers only')
            continue
    return guess 


'''Prints the amount of attempts the user has'''
def show_attempts(lives):
    print(f'You have {lives} attempts remaining to guess the number')



def number_guessing():

    print("Welcome to Number Guessing Game!\nI'm thinking of a number between 1 and 100")
    attempts = difficulty_selection()
    
    while attempts > 0:
            
        show_attempts(attempts)
        user_guess = make_guess()

        if user_guess == secret_number:
            print(f"You've guessed correctly. The answer was {secret_number}")
            return 
        
        if user_guess > secret_number:
            print('Too High.')
        else: 
            print('Too Low.')
    
        attempts -= 1
        
        if attempts > 0:
            print('Guess again')

    print("You've run out of attempts. You lost!")
        
    
    
        

number_guessing() 