from art import logo 
print(logo)


operations = {
	"+": lambda x, y: x+y,
	"-": lambda x, y: x-y,
	"*": lambda x, y: x*y,
	"/": lambda x, y: x/y,
}
num1 = float(input("What's the first number?: "))
for op in operations:
	print(op)
should_continue = True

while should_continue:
	op = input("Pick an operation: ")
	num2 = float(input("What's the next number?: "))
	calculation_function = operations[op]
	ans = calculation_function(num1, num2)
	print(f"{num1} {op} {num2} = {ans}")
	

	if input(f"Type 'y' to continue calculating with {ans}, or type 'n' to exit: ") == 'y':
		num1 = ans
		should_continue = True
	else:
		should_continue = False