from replit import clear
from art import logo

print(logo)
continuebid=True
bids={}
def find_highest_bidder(bids):
    highest_bid=0
    for bid in bids:
        bid_amount=bids[bid]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=bid
    print(f"The highest bid is {winner} with a bid of ${highest_bid}")


while continuebid==True:
   
    name=input("What is your name?")
    price=int(input("What is your bidding price"))
    bids[name]=price
    print(bids)
    continuebidyesorno=input("Would you like to continue?")
    clear()
    if continuebidyesorno=="no":
        find_highest_bidder(bids)
            