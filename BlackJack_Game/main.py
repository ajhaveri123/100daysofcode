
############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import random
from art import logo
from replit import clear
##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
def blackjack_game():
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    def deal_card(cards):
        return random.choice(cards)
    #Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
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
    #Hint 6: Create a function called calculate_score() that takes a List of cards as input 
    #and returns the score. 
    #Look up the sum() function to help you do this.
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
#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

