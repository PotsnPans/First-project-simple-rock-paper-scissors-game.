import random

options = ("rock", "paper", "scissors") 

playing = True

while playing:
    computer = random.choice(options)
    player = None

    print("===============================================")
    
    # Keep asking until valid choice
    while player not in options:
        print("You need to choose Rock, Paper, or Scissors")
        player = input("Enter your choice?: ").strip().lower()

    print("===============================================")
    
    # show what computer chose
    print(f"Computer chose: {computer}")

    # Decide winner
    if player == computer:
        print("It's a Tie!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        print("Well done!")
        if player == "rock":
            print("Rock crushes scissors. You Win!")
        elif player == "scissors":
            print("Scissors slashes paper. You Win!")
        else:
            print("Paper smothers rock. You Win!")
    else:
        print("Computer wins!")
        print(f"{computer.title()} beats {player.title()}. You Lose!")

    print("===============================================")

    # Ask to play again 
    while True:
        play_again = input("Play again? (y/n): ").strip().lower()
        
        if play_again in ('y', 'yes'):
            break           
            
        elif play_again in ('n', 'no'):
            playing = False
            break           
            
        else:
            print("Please answer with 'y' or 'n' only\n")
    
    # Accept "y", "yes", "Y", "YES"
    if not play_again.startswith("y"):
        playing = False
        print("===============================================")
        print("Thanks for playing chief!")
        print("===============================================")
