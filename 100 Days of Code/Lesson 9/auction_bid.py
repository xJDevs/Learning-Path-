# Hi there. This is one of my first mini projects :)

# The idea of this project came from course 100 Days of Coding, where the teacher is guiding the students on how to develop this program. As a goal, instead, I saw how the program ran, and tried to do it by myself, without watching the instructions on where to start, what to code or what to create. 

# If you try it, I hope you enjoyt it!!!!!

# ____________________________ AUCTION BID ____________________________

# Imgaine you have a group of friends, a people or family. Are you bidding on something? You can even use it to bet. The game will ask for the name of the user, then will ask for a bid. If there are other bidders, you can pass on the computer to the next person. Nobody else can see the bid you do, but you. At the end, wins the one who bets or bids the most, and the program will display the highest bid and the person who bidded that amount. 

import os  # library to clean screen 
import art_auction

def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    return

def ask_name():
    '''
    Will validate no blank spaces entered as name. 
    Will convert to lower, and also capitalize the names entered by user 
    '''
    while True:
        name = input('What is your name?:\n').lower().strip().capitalize()
        if name != "":
            break
        else:
            print('Please enter a valid name!')
    return name

def ask_bid():
    '''
    Will try to convert the bid entered into an int number 
    If not, will pop error and keep requesting a valid input
    '''
    while True:
        bid = input('What is your bid?:\n$')
        try:
            bid_int = int(bid)
            break
        except ValueError:
            print('Please enter numbers only')
    return bid_int
    
def other_bidders():
    '''
    Will make sure user only selects '1' or '2'
    '''
    while True:
        option = input('Are there any other bidders?\nType:\n1. Yes\n2. No\n')
        if option in ('1','2'):
            break
        else:
            print('Select a valid option')
    return option


def auction_bid():
    
    bidders = {}
    while True:
        clean_screen()
        print(art_auction.logo)
        print('Welcome to the secret auction program, where you can get as greedy as you want ;)')
        name = ask_name()
        bid = ask_bid()
        bidders[name] = bid # This will push the name : bid entered by user to the empty dictionary 
     
        other_players = other_bidders()

        if other_players == '2':
            highest_bid = -1 # initializes in -1 to protect the logic. If someone bids 0, the if below inside the loop will never execute. Nobody will bid/bet -1, hence there is always going to be something bigger than -1 

            winners = [] # Winners will be stored here. This will be used mostly to find draws 

            for key, value in bidders.items():  # .items() access both key : value 
                if value > highest_bid: 
                    highest_bid = value
                    winners = [key] # if there is only one winner, winners = 1 person
                elif value == highest_bid:
                    winners.append(key) # if multiple bids are equal, they are saved into a list to detect a draw 
                else:
                    continue

            if len(winners) > 1:
                input("We can't have several winners. Let's bid again")
                continue
            else:            
                print(f'The winner is {winners[0]} with a bid of ${highest_bid}')
            return 
        else:
            continue
            

auction_bid()
