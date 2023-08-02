#1. Create a greeting for your program.
print("Greetings! This is band-name-generator script.")
#2. Ask the user for the city that they grew up in.
city = input("Enter the city where you grew up in:\n")
#3. Ask the user for the name of a pet.
pet_name = input("Enter the name of your pet:\n")
#4. Combine the name of their city and pet and show them their band name.
print("Your band name:")
#5. Make sure the input cursor shows on a new line:
print(f"{city.title()}{pet_name.title()}")