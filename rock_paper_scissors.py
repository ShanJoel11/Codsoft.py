import random
def determine_winner(user_input, computer_choice):
  if user_input == computer_choice:
    return "tie"
  if user_input == "rock" and computer_choice == "scissors":
    return "user"
  elif user_input == "scissors" and computer_choice == "paper":
    return "user"
  elif user_input == "paper" and computer_choice == "rock":
    return "user"
  else:
    return "computer"
print("Welcome to Rock, Paper, Scissors!")
while True:
  print("\n*Rules:*")
  print("* Rock compress Scissors")
  print("* Scissors cut Paper")
  print("* Paper over the Rock")
  print("\n*How to play:*")
  print("* Enter 'rock', 'paper', or 'scissors' to choose as input.")
  user_input = input("\nChoose rock, paper, or scissors: ").lower()
  valid_choices = ["rock", "paper", "scissors"]
  while user_input not in valid_choices:
    user_input = input("Invalid choice. Please choose rock, paper, or scissors: ").lower()
  computer_choice = random.choice(valid_choices)
  print("\nYou choice:", user_input)
  print("Computer choice:", computer_choice)
  winner = determine_winner(user_input, computer_choice)
  if winner == "user":
    print("\nCongratulations! You win!")
  elif winner == "computer":
    print("\nOh no! You lost.")
  else:
    print("\nIt's a tie!")
  play_again = input("\nPlay again? (1/2): ").lower()
  if play_again != "1":
    print("\nThanks for playing!")
    break  
