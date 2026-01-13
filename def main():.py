import random 

options = ("rock", "scissors", "paper").lower()

playing = True

while playing:

    player = None
    computer = random.choice(options)

    while player not in options:
        print("You need to choose Rock, Paper, or Scissors")
        player = input("Enter your choice choice?: ")

    if player == computer:
        print("It's a Tie")
    elif player == "rock" and computer == "scissors":
        print("Well done, rock crushes scissors. You Win!")
    elif player == "scissors" and computer == "paper":
        print("Well done, scissors slashes paper. You Win!")
    elif player == "paper" and computer == "rock":
        print("Well done, paper smothers rock. You win!")
    else:
        print("Computer chose: {computer}. You Lose!")
    
    play_again = input("Would you like to play again? ").lower()
    if not play_again == "yes":
        playing = False
        
player = (f"player: {player}")
computer = (f"computer: {computer}")
    
print("Thanks for playing chief!")





