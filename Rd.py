import random
import time

def get_random_choice():
    """Generate a random choice of rock, paper, or scissors."""
    choices = ['r', 'p', 's']
    return random.choice(choices)

def determine_winner(player1_choice, player2_choice):
    """Determine the winner of the game between two players."""
    if player1_choice == player2_choice:
        return "It's a tie!"
    elif (
        (player1_choice == 'r' and player2_choice == 's') or
        (player1_choice == 'p' and player2_choice == 'r') or
        (player1_choice == 's' and player2_choice == 'p')
    ):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

def play_game():
    """Play a two-player local game of rock-paper-scissors."""
    print("Let's play Rock-Paper-Scissors!")
    wins_player1 = 0
    wins_player2 = 0

    while True:
        print("Get ready...")
        time.sleep(1)
        print("Rock...")
        time.sleep(1)
        print("Paper...")
        time.sleep(1)
        print("Scissors...")
        time.sleep(1)
        print("Shoot!")

        player1_choice = get_random_choice()
        player2_choice = get_random_choice()

        result = determine_winner(player1_choice, player2_choice)

        print("Result: ")
        time.sleep(1)
        print(result)

        print(f"Player 1 chose: {player1_choice}")
        print(f"Player 2 chose: {player2_choice}")

        if result == "Player 1 wins!":
            wins_player1 += 1
        elif result == "Player 2 wins!":
            wins_player2 += 1

        print(f"Player 1 wins: {wins_player1} Player 2 wins: {wins_player2}")

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            break

    print("Thanks for playing!")

play_game()