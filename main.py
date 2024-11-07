from Environment.Maze import Maze
import pygame
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

testMaze = Maze()

# pygame setup
pygame.init()
screen = pygame.display.set_mode((672, 744))
clock = pygame.time.Clock()
running = True

# Define colors
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Define cell size (assuming a 28x31 grid, adjust if needed)
CELL_SIZE = 24  # This gives 28 columns by 31 rows for a screen size of 672x744

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mazeImg = pygame.image.load('Environment/Maze.png')
    mazeImg = pygame.transform.scale(mazeImg, (672, 744))

    # fill the screen with a color to wipe away anything from last frame
    screen.blit(mazeImg, (0, 0))

    rowIndex = 0

    # Draw each cell based on its type
    rowIndex = 0
    for row in testMaze.rows:
        colIndex = 0
        for cell in row:
            if cell.type == "Wall":
                # Calculate the top-left corner of the cell
                x = colIndex * CELL_SIZE
                y = rowIndex * CELL_SIZE

                # Draw only the outline of the wall cell
                pygame.draw.rect(screen, BLUE, (x, y, CELL_SIZE, CELL_SIZE), 1)  # 1-pixel outline

            colIndex += 1
        rowIndex += 1

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()

