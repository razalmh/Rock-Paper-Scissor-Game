import random

from random import randint

import random

# Initialize scores
score_for_computer = 0
score_for_you = 0

# Mapping numbers to choices
number = {0: "rock", 1: "paper", 2: "scissor"}

# Game confirmation loop
while True:
    confirmation = input("Are you ready for the rock paper scissor game? (yes or no): ").lower()
    if confirmation == "yes":
        print("Let's move on! It will take little time!")
        break
    elif confirmation == "no":
        print("Let's try tomorrow.")
        exit()  # Exit the game if user says "no"
    else:
        print("You provided wrong information, try again (yes or no):")

# Main game loop
while True:
    # User input
    user_data = input("Provide input (rock, paper, or scissor): ").lower()

    # Validate user input
    if user_data not in number.values():
        print("Invalid input. Please enter rock, paper, or scissor.")
        continue

    # Generate computer choice
    computer_choice = number[random.randint(0, 2)]
    print(f"Computer chose: {computer_choice}")

    # Determine winner
    if user_data == computer_choice:
        print("It's a tie!")
    elif (user_data == "rock" and computer_choice == "scissor") or \
         (user_data == "paper" and computer_choice == "rock") or \
         (user_data == "scissor" and computer_choice == "paper"):
        print("User got 1 point!")
        score_for_you += 1
    else:
        print("Computer got 1 point!")
        score_for_computer += 1

    # Display scores
    print(f"Score - You: {score_for_you}, Computer: {score_for_computer}")

    # Ask if the user wants to continue
    play_again = input("Do you want to play again? (yes or no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! Final scores:")
        print(f"You: {score_for_you}, Computer: {score_for_computer}")
        break
