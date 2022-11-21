import random


def get_choices():
    player_choice = input("Enter a choice {rock, paper, scissors} ")
    options = ["rock", "paper", "scissor"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    print(choices)
    return choices


def check_win(player, computer):
    # print("you chose " + player + " compuer chose " + computer)
    #print(f"you chose  {player} compuer chose {computer}")

    if player == computer:
        return "It's a tie!"

    elif player == 'rock':
        if computer == "scissors":
            return "Rock smashes scessors you Won!"

        else:
            return "Paper covers rock you Lose."

    elif player == 'paper':
        if computer == "rock":
            return "Paper covers rock you Win!"

        else:
            return "Scissor cuts paper you Lose"

    elif player == 'scissors':
        if computer == "paper":
            return "Scissor cuts paper  you Win!"

        else:
            return "Rock smashs scissors you Lose"


choices = get_choices()
result = check_win(choices["player"], choices["computer"])

print(result)
