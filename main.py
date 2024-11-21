from Environment.Maze import Maze
import pygame
import os
import time
import sys
# This is a sample Python script.

pygame.init()
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
WINDOW_WIDTH = os.getenv("WINDOW_WIDTH", 672)
WINDOW_HEIGHT = os.getenv("WINDOW_HEIGHT", 792)
MOVE_AMOUNT = os.getenv("MOVE_AMOUNT", 5)
BACKGROUND_COLOR = (0, 0, 0)
TEXT_COLOR = (255, 255, 0)
BUTTON_COLOR = (50, 50, 200)
BUTTON_HOVER_COLOR = (100, 100, 255)

# FONTS
# Fonts
pygame.font.init()
TITLE_FONT = pygame.font.Font(None, 80)  # Default Pygame font
BUTTON_FONT = pygame.font.Font(None, 50)

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pacman")
clock = pygame.time.Clock()
running = True

def render_text(text, font, color, position):
    surface = font.render(text, True, color)
    rect = surface.get_rect(center=position)
    return surface, rect

# Pacman animation
def draw_pacman_animation(surface, frame):
    # Pacman mouth animation
    angle = (30 * abs(frame % 40 - 20) / 20)  # Open and close cycle
    pacman_color = (255, 255, 0)
    pacman_radius = 50
    pacman_center = (400, 400)

    # Draw pacman
    pygame.draw.circle(surface, pacman_color, pacman_center, pacman_radius)
    pygame.draw.polygon(surface, BACKGROUND_COLOR, [
        pacman_center,
        (pacman_center[0] + pacman_radius, pacman_center[1] - angle),
        (pacman_center[0] + pacman_radius, pacman_center[1] + angle)
    ])

# Main menu loop
def home_screen():
    clock = pygame.time.Clock()
    running = True
    selected_algorithm = None
    buttons = [
        {"label": "DFS", "rect": pygame.Rect(300, 200, 200, 60), "algorithm": "dfs"},
        {"label": "BFS", "rect": pygame.Rect(300, 280, 200, 60), "algorithm": "bfs"},
        {"label": "UCS", "rect": pygame.Rect(300, 360, 200, 60), "algorithm": "ucs"},
        {"label": "A*", "rect": pygame.Rect(300, 440, 200, 60), "algorithm": None},
    ]

    while running:
        screen.fill(BACKGROUND_COLOR)

        # Draw title
        title_surface, title_rect = render_text("Select Algorithm", TITLE_FONT, TEXT_COLOR, (WINDOW_WIDTH // 2, 100))
        screen.blit(title_surface, title_rect)

        # Draw buttons
        mouse_pos = pygame.mouse.get_pos()
        for button in buttons:
            # Change color on hover
            color = BUTTON_HOVER_COLOR if button["rect"].collidepoint(mouse_pos) else BUTTON_COLOR
            pygame.draw.rect(screen, color, button["rect"])
            # Draw button label
            label_surface, label_rect = render_text(button["label"], BUTTON_FONT, TEXT_COLOR, button["rect"].center)
            screen.blit(label_surface, label_rect)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button["rect"].collidepoint(event.pos):
                        selected_algorithm = button["algorithm"]
                        running = False  # Exit the menu loop

        # Update the screen
        pygame.display.flip()
        clock.tick(60)

    return selected_algorithm

selected_algorithm = home_screen()
# pygame setup

testMaze = Maze(48, selected_algorithm)

# Define cell size (assuming a 28x31 grid, adjust if needed)
CELL_SIZE = os.getenv("CELL_SIZE", 24)  # This gives 28 columns by 31 rows for a screen size of 672x744
move = 0
game_over = False
while running and not game_over:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    mazeImg = pygame.image.load('Environment/Maze.png')
    mazeImg = pygame.transform.scale(mazeImg, (672, 744))

    # fill the screen with a color to wipe away anything from last frame
    screen.blit(mazeImg, (0, 48))

    rowIndex = 0

    testMaze.moveEntities()
    testMaze.draw(screen)
    # flip() the display to put your work on screen
    pygame.display.flip()
    time.sleep(.1)
    if testMaze.isOver():
        game_over = True

    clock.tick(60)  # limits FPS to 60


RED = (255, 0, 0)

pygame.display.set_caption("Game Over!")

font = pygame.font.Font('Quinquefive-ALoRM.ttf', 24)

# Render the text
text = font.render("Game over, you won!", True, RED)

# Get the text's rectangle for centering
text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))

# Create a background rectangle slightly larger than the text
background_rect = text_rect.inflate(25, 25)

# Draw the background rectangle
pygame.draw.rect(screen, (171, 178, 191), background_rect)

screen.blit(text, text_rect)

pygame.display.flip()

time.sleep(5)

pygame.quit()

