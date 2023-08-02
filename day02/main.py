#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
if __name__ == "__main__":
	print("Welcome to tip calculator!")
	bill = float(input("Enter the bill value: $"))
	persons_number = int(input("Enter the number of persons to split: "))
	tip = int(input("Enter the tip amount in procents: "))
	pay_value = (bill / persons_number) * (tip / 100 + 1)
	print(f"Each person shoud pay: ${pay_value:.2f}")