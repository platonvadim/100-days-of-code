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

#Write your code below this line 👇
def main():
    print("Welcome to the rock, paper, scissors game.")
    player_choice = input("Choose rock, paper or scissors: ").lower()
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    image = [rock, paper, scissors]
    image_name =['rock', 'paper', 'scissors']
    print(f"You:\n{image[image_name.index(player_choice)]}")
    print(f"Computer:\n{image[image_name.index(computer_choice)]}")
    chooses_str = f"You choosed {player_choice}.\nComputer choosed {computer_choice}."

    if player_choice == computer_choice:
        print(f"{chooses_str}.\nDraft.")
    elif player_choice == 'rock':
        if computer_choice == "paper":
            print(f"{chooses_str}.\nYou lose.")
        elif computer_choice == "scissors":
            print(f"{chooses_str}.\nYou win.")

    elif player_choice == 'paper':
        if computer_choice == "rock":
            print(f"{chooses_str}.\nYou win.")
        elif computer_choice == "scissors":
            print(f"{chooses_str}.\nYou lose.")

    elif player_choice == 'scissors':
        if computer_choice == "rock":
            print(f"{chooses_str}.\nYou lose.")
        elif computer_choice == "paper":
            print(f"{chooses_str}.\nYou win.")
    input("Game Over.")

if __name__ == '__main__':
    main()