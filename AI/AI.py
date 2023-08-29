import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 640, 480
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock Paper Scissors")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define game variables
FPS = 60
clock = pygame.time.Clock()

# Define button class
class Button:
    def __init__(self, x, y, width, height, text, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = WHITE
        self.text = text
        self.action = action

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)
        font = pygame.font.Font(None, 36)
        text = font.render(self.text, True, BLACK)
        text_rect = text.get_rect(center=self.rect.center)
        win.blit(text, text_rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

    def perform_action(self):
        if self.action:
            self.action()

# Create buttons
buttons = [
    Button(50, 150, 80, 80, "Rock", action=lambda: make_choice("rock")),
    Button(250, 150, 80, 80, "Paper", action=lambda: make_choice("paper")),
    Button(450, 150, 80, 80, "Scissors", action=lambda: make_choice("scissors"))
]

player_choice = None
computer_choice = None
result = None

def make_choice(choice):
    global player_choice, computer_choice, result

    player_choice = choice
    computer_choice = random.choice(["rock", "paper", "scissors"])

    # Determine the winner
    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
            (player_choice == "paper" and computer_choice == "rock") or \
            (player_choice == "scissors" and computer_choice == "paper"):
        result = "You win!"
    else:
        result = "Computer wins!"

# Game loop
running = True
while running:
    clock.tick(FPS)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            for button in buttons:
                if button.is_clicked(mouse_pos):
                    button.perform_action()

    # Clear the screen
    win.fill(WHITE)

    # Draw buttons
    for button in buttons:
        button.draw(win)

    # Display the result
    if result:
        font = pygame.font.Font(None, 36)
        text = font.render(result, True, BLACK)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
        win.blit(text, text_rect)

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()