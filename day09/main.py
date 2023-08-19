import os
from art import logo

print(logo)
print("Welcome to the secret auction program. ")
name = input("What is your name?: ")
bid = int(input("What is your bid?: $"))
ans = input("Are there any other bidders? Type 'yes' or 'no'.\n")
bids = dict()
bids.update({name: bid})

while ans != "no":
	os.system('cls')
	name = input("What is your name?: ")
	bid = int(input("What is your bid?: $"))
	bids.update({name: bid})
	ans = input("Are there any other bidders? Type 'yes' or 'no'.\n")

highest_bid = 0
for key in bids:
	print(key, bids[key])
	if bids[key] > highest_bid:
		highest_bid = bids[key]
		name = key
print(f"The winner is {name} with a bid of ${highest_bid}")
input()