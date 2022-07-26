import art
import random
from game_data import data

print(art.logo)


def random_account():
    return random.choice(data)

def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
        
def game():
    points=0
    game_over=False
    account_a=random_account()
    account_b=random_account()
    
    while game_over==False:
        
        print(format_data(account_a))
        print("vs")
        print(format_data(account_b))
    
        guess = input("Who has more followers? A or B?").lower()
        a_follower_count=account_a["follower_count"]
        b_follower_count=account_b["follower_count"]
        user_correct=check_answer(guess, a_follower_count, b_follower_count)
        
        if user_correct == False:
            print(f"You're wrong, game over. Your score is {points}")
            game_over = True
        
        else:
            points += 1
            print(f"Correct! +1 points :) You now have {points} point(s).")
            account_a=account_b
            account_b=random_account()
game()