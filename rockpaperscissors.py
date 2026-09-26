import random

valid_choices = ["rock", "paper", "scissors"]

while True:
    player1 = input("Select Rock, Paper, or Scissor :"). lower()
    if player1 not in valid_choices:
        print("Invalid choice! Please type out the full word. (rock, paper, or scissors).\n")
        continue
    player2 = random.choice(["Rock", "Paper", "Scissor"]).lower()
    print("Player 2 Selected: ", player2)

    if player1 == "rock" and player2 == "paper":
        print("Player 2 Won")
    elif player1 == "paper" and player2 == "scissors":
        print("Player 2 Won")
    elif player1 == "scissors" and player2 == "rock":
        print("Player 2 Won")
    elif player1 == player2:
        print("Tie")
    else:
        print("Player 1 Won")

    play_again = input("\nDo you want to play again? (yes/no) :").lower()
    if play_again != "yes" and play_again != "y":
        print("Thanks for playing! See you again.")
        break