"""
Program: High-Low Game

This program is a simple guessing game. The player sees their number and guesses
whether it is higher or lower than the computer's hidden number.

The game runs for multiple rounds, tracks the score, and prints a final message
based on the player's performance.

Concepts practiced:
- Random numbers
- Constants
- For loops
- While loops
- If / else statements
- Boolean logic
- Score tracking
- Input validation
"""

# Code in Place IDE demo:
# Open this link and click Run to execute the program in the CIP IDE.
# https://codeinplace.stanford.edu/cip6/share/GN3qMgjbF6Lw3pgBoT36

import random

NUM_ROUNDS = 5


def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')

    # Start the score at zero before the rounds begin
    your_score = 0

    # Repeat the game for the number of rounds set above
    for i in range(NUM_ROUNDS):
        print(f"Round {i + 1}")

        # Create one hidden number for the computer and one visible number for the player
        computer_num = random.randint(1, 100)
        your_num = random.randint(1, 100)
        print(f"Your number is {your_num}")

        # Ask the player to guess if their number is higher or lower
        choice = input("Do you think your number is higher or lower than the computer's?: ")

        # Keep asking until the player types a valid option
        while choice != "higher" and choice != "lower":
            choice = input("Please enter either higher or lower: ")

        # Store the winning conditions in variables to make the if statement easier to read
        higher_and_correct = choice == "higher" and your_num > computer_num
        lower_and_correct = choice == "lower" and your_num < computer_num

        if higher_and_correct or lower_and_correct:
            print(f"You were right! The computer's number was {computer_num}")
            your_score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_num}")

        print(f"Your score is now {your_score}")
        print()

    # Print the final score and a message based on the player's result
    print(f"Your final score is {your_score}")

    if your_score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif your_score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")


if __name__ == "__main__":
    main()
