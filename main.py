from Environment.Maze import Maze
import pygame
import os
import time
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
WINDOW_WIDTH = os.getenv("WINDOW_WIDTH", 672)
WINDOW_HEIGHT = os.getenv("WINDOW_HEIGHT", 792)
MOVE_AMOUNT = os.getenv("MOVE_AMOUNT", 5)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# pygame setup
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
running = True
testMaze = Maze(48)


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

    time.sleep(0.25)
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

