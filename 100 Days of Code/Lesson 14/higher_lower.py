''' 
This is a curious project that compares amounts of followers of Instagram accounts. 
The user will have to guess which account has more followers. If guessed correctly, scores a point, otherwise, the game ends.
'''

import art
import data
import random
import os 

data = data.data
logo = art.logo
vs_logo = art.vs

def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    return

'''Will ask user to enter strictly A or B'''
def ask_who():

    while True:
        a_or_b = input('Who has more followers? Type A or B\n').capitalize()
        if a_or_b not in ('A','B'):
            print("Please enter 'A' or 'B' only")
            continue
        else:
            return a_or_b

'''Will return an a or an depending on the starting letter of the given string'''

def article(word):
    if word[0].lower() in 'aeiou':
        return 'an'
    return 'a'


score = 0 # Will carry out the correct responses of the user 
is_answer_correct = True # Boolean that will keep the loop
while is_answer_correct:

    correct_answer = False # This will prompt a print with the score of the user if the answer is correct 

    '''These 2 variables will generate a number between 0 and 49 which will be passed as index to access data from the list of the dictionary'''
    index_A = random.randint(0, 49)
    index_B = random.randint(0, 49)

    ''' In case A and B are equal, it will generate a new index for B'''
    while index_A == index_B:
        index_B = random.randint(0, 49)

    '''Since we will be working with a dictionary for each option A and B, a dictionary for each option is instanced'''

    option_A = data[index_A]
    information_A = {
        'account': option_A['name'],
        'description': option_A['description'],
        'country': option_A['country'],
        'followers': option_A['follower_count']
    }
    
    option_B = data[index_B]
    information_B = {
        'account': option_B['name'],
        'description': option_B['description'],
        'country': option_B['country'],
        'followers': option_B['follower_count']
    }

        
    clean_screen()
    print(logo)

    if correct_answer:
        print(f'You are right! Current score {score}')

    print(f'Compare A: {information_A["account"]}, {article(information_A["description"])} {information_A['description']}, from {information_A["country"]}')
    print(vs_logo)
    print(f'Against B: {information_B["account"]}, {article(information_B["description"])} {information_B['description']}, from {information_B["country"]}')
    user_answer = ask_who()

    if user_answer == 'B':
        guessed_followers = information_B['followers']
        if guessed_followers > information_A['followers']:
            correct_answer = True
            score +=1
        else:
            is_answer_correct = False
            print(f"Sorry, that's wrong! Final score {score}")
    else:
        guessed_followers = information_A['followers']
        if guessed_followers > information_B['followers']:
            correct_answer = True
            score +=1
        else:
            is_answer_correct = False
            print(f"Sorry, that's wrong! Final score {score}")
        
    