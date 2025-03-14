# Day 38
# Guess a Number

import random as rd


def guess_a_number():
    # Generate a random number between 1 and 10
    number = rd.randrange(1, 11)
    # Set the number of attempts the player has
    attempts_remaining = 3

    while attempts_remaining > 0:
        print(f"You have {attempts_remaining} attempt(s) remaining.")
        guess_num = int(input("Guess a number between 1 and 10: "))

        if guess_num == number:
            print("** Congratulations! You guessed the correct number. **")
            break
        elif guess_num > number:
            print("** Your guess is too high. **")
            attempts_remaining -= 1
        else:
            print("** Your guess is too low. **")
            attempts_remaining -= 1
    else:
        # This block executes if the loop ends without breaking (i.e., the player runs out of attempts)
        print("** You lost the game! **")
        print(f"The correct number was {number}.")


# Call the function to start the game
guess_a_number()