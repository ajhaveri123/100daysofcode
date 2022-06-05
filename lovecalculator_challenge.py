# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combinedname=name1+name2

lowercombinedname=combinedname.lower()
t=lowercombinedname.count("t")
r=lowercombinedname.count("r")
u=lowercombinedname.count("u")
e=lowercombinedname.count("e")
true=t+r+u+e
l=lowercombinedname.count("l")
o=lowercombinedname.count("o")
v=lowercombinedname.count("v")
e=lowercombinedname.count("e")
love=l+o+v+e

score = int(str(true) + str(love))

if score<10 or score>90:
    print(f"Your score is {score}, you go together like coke and mentos.")

elif score>40 and score<50:
    print (f"Your score is {score}, you are alright together.")

else:
    print (f"Your score is {score}.")
