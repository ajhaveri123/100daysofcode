import random
logo ="""  
  __ _ _   _  ___  ___ ___   _ __ ___  _   _   _ __  _   _ _ __ ___ | |__   ___ _ __ 
 / _` | | | |/ _ \/ __/ __| | '_ ` _ \| | | | | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
| (_| | |_| |  __/\__ \__ \ | | | | | | |_| | | | | | |_| | | | | | | |_) |  __/ |   
 \__, |\__,_|\___||___/___/ |_| |_| |_|\__, | |_| |_|\__,_|_| |_| |_|_.__/ \___|_|   
 |___/                                 |___/                                                    
"""

print(logo)
print("Welcome to 'Guess my number'")

def attempts_per_mode():
    mode=input("Type easy or hard")
    if mode=="easy":
        print("You have 10 attempts")
        attempts=10
        return attempts
    else:
        print("You have 5 attempts")
        attempts=5
        return attempts
        
attempts=attempts_per_mode()

rnum = random.randint(1,100)
print(f"Psst the number is {rnum}, this is for testing purposes")

def game(attempts, rnum):
    guess_is_correct=False
    while attempts>0 and guess_is_correct==False:
        guess=int(input("Make a guess: "))
        if guess==rnum:
            guess_is_correct=True
            print(f"Correct! The number is {rnum}!")
        else:
            if guess>rnum:
                print("Too high.")
            elif guess<rnum:
                print("Too low.")
            attempts-=1
            if attempts==0:
                print("You're out of attempts! You lose.")
            else:
                print(f"You have {attempts} attempts left")
game(attempts, rnum)

