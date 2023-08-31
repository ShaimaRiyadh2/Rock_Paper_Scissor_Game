import random

def play_game():
    attempts = 6
    user_wins = 0  # Number of user wins
    computer_wins = 0  # Number of computer wins
    choices = {
        1: "Rock",
        2: "Paper",
        3: "Scissor"
    }

    print("Welcome To Rock Paper Scissor Game \n Done By Shaima Riyadh" )

    while attempts > 0:
        print("Number of attempts", attempts)
        print("Available choices:")
        for key, value in choices.items():
            print(f"{key}. {value}")

        player_choice = int(input("Choose your option (1-3): "))
        if player_choice not in choices:
            print("Invalid choice!")
            continue

        player_choice = choices[player_choice]
        computer_choice = random.choice(list(choices.values()))

        print("Your choice:", player_choice)
        print("Computer's choice:", computer_choice)

        attempts -= 1
        
        if player_choice == computer_choice:
            print("It's a tie!")  # It's a tie
        elif (player_choice == "Rock" and computer_choice == "Scissor") or \
                (player_choice == "Scissor" and computer_choice == "Paper") or \
                (player_choice == "Paper" and computer_choice == "Rock"):
            print("You win!")  # User wins
            user_wins += 1  # Increase user wins by 1
        else:
            print("Computer wins!")  # Computer wins
            computer_wins += 1  # Increase computer wins by 1

    print("Game over.")
    print("User wins:", user_wins)  # Display number of user wins
    print("Computer wins:", computer_wins)  # Display number of computer wins

    if user_wins > computer_wins:
        print("Congratulations! You beat the computer!")  # User is the winner
    elif user_wins < computer_wins:
        print("Oops! The computer beat you.")  # Computer is the winner
    else:
        print("It's a tie! No one wins.")  # It's a tie

play_game()