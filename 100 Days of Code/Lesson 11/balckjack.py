import os
import random


def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    return

def yes_or_no():
    valid_options = ('1', '2')
    while True:
        choice = input('1. Yes\n2. No\n')
        if choice not in valid_options:
            print('Please enter a valid option (1 or 2)')
            continue
        else:
            return choice 
        
def sum_score(deck):
    total = 0
    for i in deck:
        total += i
    return total 

def ace(deck):
    score = sum_score(deck)
    for card in range(len(deck)):
        if deck[card] == 11 and score > 21:
            deck[card] = 1
            score -= 10
    return score 

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

target = 21

def blackjack():

    game_over = False 
    while not game_over:

        user_deck = []
        computer_deck = []
        user_score = 0
        computer_score = 0

        print("Do you want to start a new BlackJack game?")
        new_game = yes_or_no()
        clean_screen()

        if new_game == '2':
            print("Thank you for playing BlackJack at Joe's. Comeback soon!")
            return 
        else: 
            for _ in range(2):
                user_deck.append(random.choice(cards))
            computer_deck.append(random.choice(cards))
            user_score = ace(user_deck)
            print(f"Your cards: {user_deck}. Current score: {user_score}\nComputer's first card: {computer_deck}")

        another_card = True
        while another_card:
            print('Do you want to draw another card?:')
            draw_card = yes_or_no()
            computer_score = ace(computer_deck)

            if draw_card == '1':
                user_deck.append(random.choice(cards))
                user_score = ace(user_deck)
            
                if user_score > target:
                    print(f"Your cards: {user_deck}. Current score: {user_score}\nComputer's first card: {computer_deck}\nYour final hand: {user_deck}\nComputer's final hand: {computer_score}\nYou went over {target}. You lose!\n")
                    another_card = False 
                    
                elif user_score < target:
                    print(f"Your cards: {user_deck}. Current score: {user_score}\nComputer's first card: {computer_deck}")
                    continue
                

            else:
                computer_draws = [True, False]
                computer_decision = random.choice(computer_draws)
                times = [1, 2, 3]
                if computer_decision == True:
                    computer_score = ace(computer_deck)
                    if computer_score < target:
                        for _ in range(random.choice(times)):
                            computer_deck.append(random.choice(cards))
                            computer_score = ace(computer_deck)

                if computer_score > user_score:
                    print(f"Your final hand: {user_deck}. Current score: {user_score}\nComputer's final hand: {computer_deck}\nCumputer Score: {computer_score}\nYou Win!\n") 
                elif computer_score > target:
                    print(f"Your final hand: {user_deck}. Current score: {user_score}\nComputer's final hand: {computer_deck}. Computer's final score: {computer_score}\nComputer went over {target}. You Win!\n")
                elif computer_score == user_score:
                    print(f"Your final hand: {user_deck}. Current score: {user_score}\nComputer's final hand: {computer_deck}. Computer's final score: {computer_score}\nDRAW!\n")
                elif computer_score == target:
                    print(f"Your final hand: {user_deck}. Current score: {user_score}\nComputer's final hand: {computer_deck}. Computer's final score: {computer_score}\nComputer has BlackJack. You Lose!\n") 
                elif user_score == target:
                    print(f"Your final hand: {user_deck}. Current score: {user_score}\nComputer's final hand: {computer_deck}. Computer's final score: {computer_score}\nBlackJack. You Win!\n") 
                else:
                    print(f"Your final hand: {user_deck}. Current score: {user_score}\nComputer's final hand: {computer_deck}. Computer's final score: {computer_score}\nYou Win!\n")
                break  



blackjack()


