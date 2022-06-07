import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice=int(input("Choose 1, 2, or 3 for rock, paper, or scissors."))

if choice==1:
  print(f"You chose: {rock}")
elif choice==2:
  print(f"You chose: {paper}")
elif choice==3:
  print(f"You chose: {scissors}")
else:
  print("Invalid Input.")

computeroptions=[rock, paper, scissors]
randomchoice=random.randint(1,3)

print(f"\nComputer chooses:{computeroptions[randomchoice-1]}")

if (choice==1 and randomchoice==1) or (choice==2 and randomchoice==2) or (choice==3 and randomchoice==3):
  print("It's a tie!")

elif (choice==1 and randomchoice==2) or (choice==2 and randomchoice==3) or (choice==3 and randomchoice==1):
 print("You lose!")

elif (choice==1 and randomchoice==3) or (choice==2 and randomchoice==1) or (choice==3 and randomchoice==2):
 print("You win!")
        
