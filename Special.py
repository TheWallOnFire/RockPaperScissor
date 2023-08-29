import random

def get_user_choice():
    """Get the user's choice of rock, paper, scissors, lizard, or Spock."""
    while True:
        user_choice = input("Enter your choice (r/p/s/l/sp): ").lower().replace(" ", "")
        if user_choice in ['r', 'p', 's', 'l', 'sp']:
            return user_choice
        else:
            print("Invalid choice. Please try again.")

def get_computer_choice():
    """Generate a random choice for the computer."""
    choices = ['r', 'p', 's', 'l', 'sp']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determine the winner of the game."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == 'r' and (computer_choice == 'l' or computer_choice == 's')) or
        (user_choice == 'p' and (computer_choice == 'r' or computer_choice == 'sp')) or
        (user_choice == 's' and (computer_choice == 'p' or computer_choice == 'l')) or
        (user_choice == 'l' and (computer_choice == 'sp' or computer_choice == 'p')) or
        (user_choice == 'sp' and (computer_choice == 'r' or computer_choice == 's'))
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_again():
    """Ask the user if they want to play again."""
    while True:
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again in ['y', 'n']:
            return play_again == 'y'
        else:
            print("Invalid choice. Please try again.")

def play_game():
    """Play a game of rock-paper-scissors-lizard-Spock."""
    print("Let's play Rock-Paper-Scissors-Lizard-Spock!")
    wins = 0
    losses = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            wins += 1
        elif result == "Computer wins!":
            losses += 1

        print(f"Wins: {wins} Losses: {losses}")

        if not play_again():
            break

    print("Thanks for playing!")

play_game()