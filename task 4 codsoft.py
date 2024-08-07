import random
def determine_winner(user_choice, computer_choice):
  """Compares user and computer choices to determine winner."""
  wins = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
  return "tie" if user_choice == computer_choice else (
      "user" if wins[user_choice] == computer_choice else "computer"
  )
print("Welcome to Rock, Paper, Scissors!")
while True:
  print("\n**Rules:**\nRock > Scissors\nScissors > Paper\nPaper > Rock")
  print("\n**How to play:**\nEnter 'rock', 'paper', or 'scissors' to choose.")
  user_choice = input("\nChoose rock, paper, or scissors: ").lower()
  valid_choices = ["rock", "paper", "scissors"]
  while user_choice not in valid_choices:
    user_choice = input("Invalid choice. Please choose rock, paper, or scissors: ").lower()
  computer_choice = random.choice(valid_choices)
  print(f"\nYou chose: {user_choice}\nComputer chose: {computer_choice}")
  winner = determine_winner(user_choice, computer_choice)
  print(f"\n{winner.capitalize()} wins!") if winner != "tie" else print("\nIt's a tie!")
  play_again = input("\nPlay again? (y/n): ").lower()
  if play_again != "y":
    print("\nThanks for playing!")
    break

