import tkinter as tk
from tkinter import messagebox
import random

# Global variables
player_score = 0
computer_score = 0

# Function to check the winner and update points
def determine_winner(user_choice):
    global player_score, computer_score

    computer_choice = random.choice(["rock", "paper", "scissors"])

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        result = "You win!"
        player_score += 1
    else:
        result = "You lose!"
        computer_score += 1

    update_score()
    messagebox.showinfo("Result", f"Computer chose {computer_choice}.\n{result}")

# Function to handle button clicks
def button_click(choice):
    determine_winner(choice)

# Function to update the score on the screen
def update_score():
    score_label.config(text=f"Player: {player_score}  Computer: {computer_score}")

# Function to start a new game
def restart_game():
    global player_score, computer_score

    player_score = 0
    computer_score = 0
    update_score()
    show_tutorial()

# Function to start the game
def start_game():
    intro_label.pack_forget()
    start_button.pack_forget()
    restart_button.pack()
    show_tutorial()

# Function to show the tutorial
def show_tutorial():
    tutorial_text = "Welcome to Rock-Paper-Scissors!\n\n"
    tutorial_text += "Click on one of the buttons below to make your choice.\n"
    tutorial_text += "Rock beats scissors, scissors beat paper, and paper beats rock.\n\n"
    tutorial_text += "The game has no set number of rounds. You can restart the game at any time.\n\n"
    tutorial_text += "Good luck!"

    tutorial_label.config(text=tutorial_text)
    tutorial_label.pack()
    rock_button.pack()
    paper_button.pack()
    scissors_button.pack()

# Create the main window
window = tk.Tk()
window.title("Rock-Paper-Scissors")

# Set window size
window.geometry("500x400")

# Create starting scene
intro_label = tk.Label(window, text="Welcome to Rock-Paper-Scissors Game!")
intro_label.pack()

start_button = tk.Button(window, text="Start", command=start_game)
start_button.pack()

# Create tutorial label
tutorial_label = tk.Label(window, text="")
tutorial_label.pack()

# Create buttons for rock, paper, and scissors
rock_button = tk.Button(window, text="Rock", command=lambda: button_click("rock"))
paper_button = tk.Button(window, text="Paper", command=lambda: button_click("paper"))
scissors_button = tk.Button(window, text="Scissors", command=lambda: button_click("scissors"))

# Create restart button
restart_button = tk.Button(window, text="Restart", command=restart_game)
restart_button.pack()

# Create score label
score_label = tk.Label(window, text="Player: 0  Computer: 0")
score_label.pack()

# Start the Tkinter event loop
window.mainloop()