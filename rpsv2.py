#!/usr/bin/python3
""" Rock, paper, Scissor version2"""


import random

def rock_paper_scissors():

#define the choices
    choices = ["rock", "paper", "scissors"]

    #define the rules
    rules = {
        "rock" : "scissors",
        "scissors" : "paper",
        "paper" : "rock"
    }

    #define score
    user_score = 0
    computer_score = 0

    #define number of rounds
    rounds = 3


    #start game loop
    for i in range(rounds):
        #print rounds number
        print(f"Round {i+1}")
        #get user choice
        user_choice = input("Enter rock, paper, or scissors: ").lower()
        #validate user choice
        while user_choice not in choices:
            print("Invalid choice, Please enter rock, paper, or scissors")
            user_choice = input("Enter rock, paper, or scissros: ").lower()

        #generate computer choice
        computer_choice = random.choice(choices)
        print(f"Computer chose {computer_choice}")

        #Determine and anounce winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif rules[user_choice] == computer_choice:
            print("You win!")
            user_score += 1
        else:
            print("Compouter wins!")
            computer_score += 1

        # Print the score
        print(f"Current Score - You {user_score}, Computet {computer_score}\n")

    # Determine and announce overall winner
    if user_score > computer_score:
        print("You win the game!")
    elif user_score < computer_score:
        print("You lose the game!")
    else:
        print("It's a tie!")

rock_paper_scissors()