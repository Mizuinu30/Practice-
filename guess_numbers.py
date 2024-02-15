#!/usr/bin/python3
""" function to guess a random number"""

import random

def guessarandnum():
    rand_num = random.randint(1, 100)
    attempts = 0

    while attempts < 4:
        user_guess = int(input("Guess a random number between 1 and 100: "))

        if user_guess < rand_num:
            print("Not correct, guess higher.")
        elif user_guess > rand_num:
            print("Wrong, try lower.")
        else:
            print("Congrats! You got it")
            return

        attempts += 1

    print(f"Sorry, you didn't guess it. The number was {rand_num}.")

guessarandnum()