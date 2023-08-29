import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the window
window_width = 640
window_height = 480
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Rock Paper Scissors")

# Set up colors
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up fonts
font = pygame.font.Font(None, 36)

# Set up game variables
player_choice = None
computer_choice = None
winner = None
player_points = 0
computer_points = 0

# Create buttons
button_width = 100
button_height = 100
button_margin = 30

rock_button = pygame.Rect(
    (window_width - button_width) // 2 - button_width - button_margin,
    window_height // 2 - button_height // 2,
    button_width, button_height
)
paper_button = pygame.Rect(
    (window_width - button_width) // 2,
    window_height // 2 - button_height // 2,
    button_width, button_height
)
scissors_button = pygame.Rect(
    (window_width - button_width) // 2 + button_width + button_margin,
    window_height // 2 - button_height // 2,
    button_width, button_height
)

reset_button = pygame.Rect(
    (window_width - button_width) // 2,
    window_height // 2 + button_height + button_margin,
    button_width, button_height
)

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def draw_text(text, x, y, color=WHITE):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    window.blit(text_surface, text_rect)

def draw_buttons():
    pygame.draw.rect(window, GRAY, rock_button)
    pygame.draw.rect(window, GRAY, paper_button)
    pygame.draw.rect(window, GRAY, scissors_button)

    draw_text("Rock", rock_button.centerx, rock_button.centery)
    draw_text("Paper", paper_button.centerx, paper_button.centery)
    draw_text("Scissors", scissors_button.centerx, scissors_button.centery)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Tie"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        return "Player wins"
    else:
        return "Computer wins"

def reset_game():
    global player_choice, computer_choice, winner, player_points, computer_points
    player_choice = None
    computer_choice = None
    winner = None
    player_points = 0
    computer_points = 0

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if rock_button.collidepoint(mouse_pos):
                player_choice = "rock"
            elif paper_button.collidepoint(mouse_pos):
                player_choice = "paper"
            elif scissors_button.collidepoint(mouse_pos):
                player_choice = "scissors"
            elif reset_button.collidepoint(mouse_pos):
                reset_game()

            if player_choice:
                computer_choice = get_computer_choice()
                winner = determine_winner(player_choice, computer_choice)
                if winner == "Player wins":
                    player_points += 1
                elif winner == "Computer wins":
                    computer_points += 1

    # Clear the window
    window.fill((0, 0, 0))

    # Draw buttons
    draw_buttons()

    # Draw player and computer choices
    if player_choice:
        draw_text("Player: " + player_choice, window_width // 4, 50)
    if computer_choice:
        draw_text("Computer: " + computer_choice, 3 * window_width // 4, 50)

    # Draw winner text
    if winner:
        if winner == "Tie":
            draw_text("It's a tie!", window_width // 2, 100, GRAY)
        elif winner == "Player wins":
            draw_text("Player wins!", window_width // 2, 100, GREEN)
        else:
            draw_text("Computer wins!", window_width // 2, 100, RED)

    # Draw player and computer points
    draw_text("Player Points: " + str(player_points), window_width // 4, 150)
    draw_text("Computer Points: " + str(computer_points), 3 * window_width // 4, 150)

    # Draw reset button
    pygame.draw.rect(window, GRAY, reset_button)
    draw_text("Reset", reset_button.centerx, reset_button.centery)

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()