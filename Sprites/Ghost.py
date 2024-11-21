import pygame
import os
from AI.BrainGhost import BrainGhost
from Sprites.Direction import Direction

CELL_SIZE = int(os.getenv("CELL_SIZE", 24))

# Define the Ghost class
class Ghost(pygame.sprite.Sprite):
    def __init__(self, col, row, yOffset, gameBoard, image_path="ghost.png"):
        super().__init__()
        self.col = col
        self.row = row
        self.yOffset = yOffset
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (CELL_SIZE, CELL_SIZE))
        self.brain = BrainGhost(gameBoard)  # Create Brain for Ghost

    def getPosition(self):
        return (self.row, self.col)

    def draw(self, screen):
        x = self.col * CELL_SIZE
        y = self.row * CELL_SIZE + self.yOffset
        screen.blit(self.image, (x, y))

    def move(self, pacman):
        direction = self.brain.getNextMove(pacman, self.getPosition())

        # Check the new position and update the ghost's row and column
        if direction == Direction.UP:
            self.row -= 1
        elif direction == Direction.DOWN:
            self.row += 1
        elif direction == Direction.LEFT:
            if self.getPosition() == (14, 0):
                self.col = 27
            else:
                self.col -= 1
        elif direction == Direction.RIGHT:
            if self.getPosition() == (14, 27):
                self.col = 0
            else:
                self.col += 1
