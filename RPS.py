import random 

def get_choices():
  player_choice = input("Enter a choice (rock, paper, scissors): ")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices

def check_win(player, computer):
  print(f"Player chose {player}, computer chose {computer}")
  if player == computer:
    return "It's a tie!"
  elif player == "rock" and computer == "scissors":
    return "Rock smashes scissors! You win!"
  elif player == "rock" and computer == "paper":
    return "Paper covers rock! You lose."
  elif player == "paper" and computer == "rock":
    return "Paper covers rock! You win!"
  elif player == "paper" and computer == "scissors":
    return "Scissors cuts paper! You lose."
  elif player == "scissors" and computer == "paper":
    return "Scissors cuts paper! You win!"
  elif player == "scissors" and computer == "rock":
    return "Rock smashes scissors! You lose."

choices=get_choices()
check_win(choices["player"], choices["computer"])