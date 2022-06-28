

import random
from art import logo
from replit import clear

def blackjack_game():
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    def deal_card(cards):
        return random.choice(cards)
    user_cards = []
    computer_cards = []
    for i in range (2):
        new_card=deal_card(cards)
        user_cards.append(new_card)
        new_card=deal_card(cards)
        computer_cards.append(new_card)
        
    deal_card(cards)
    print(f"user cards are: {user_cards}")
    print(f"computer cards are {computer_cards}")
    
    game_over=False
    def calculate_score(cards):
        if 11 in cards and 10 in cards and len(user_cards)==2:
            return 0
        elif 11 in cards and sum(cards)>21:
            cards.remove(11)
            cards.append(1)
        else: 
            return sum(cards)
    
    calculate_score(cards)
    
    if sum(user_cards)>21 or sum(computer_cards)>21:
        game_over=True
    
    while game_over==False:
        another_card=input("Would you like to draw another card? Type 'y' for yes and 'n' for no.")
        if another_card=='y':
            deal_card(cards)
            user_cards.append(deal_card(cards))
            print(f"Your cards are now:{user_cards}")
            calculate_score(user_cards)
        elif another_card=='n':
            game_over=True
    
    while sum(computer_cards)<17:
        computer_cards.append(deal_card(computer_cards))
        print(f"Computer dealt. It's cards are now: {computer_cards}")
    
    user_score=sum(user_cards)
    computer_score=sum(computer_cards)
    def compare(user_score, computer_score):
        if computer_score==user_score:
            print("Its a draw.")
        elif computer_score==0 or user_score>21:
            print("You lose. Computer wins.")
        elif user_score==0 or computer_score>21:
            print("You win. Computer loses.")
        else:
            if user_score>computer_score:
                print("User wins.")
            else: 
                print("Computer wins")
    
    compare(user_score, computer_score)
blackjack_game()

restart_game = input("Would you like to restart the game? Type 'y for yes and 'n' for no")
if restart_game=='y':
    clear()
    blackjack_game()
else:
    print("Thank you for playing!")


