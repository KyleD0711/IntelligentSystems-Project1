import pygame
import os

CELL_SIZE = int(os.getenv("CELL_SIZE", 24))

# Define the Ghost class
class Ghost(pygame.sprite.Sprite):
    def __init__(self, col, row, image_path="ghost.png"):
        super().__init__()
        self.col = col  # Ghost's x position
        self.row = row  # Ghost's y position

        # Load and scale the ghost image
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (CELL_SIZE, CELL_SIZE))

    def getPosition(self):
        return (self.col, self.row)

    def draw(self, screen):
        # Calculate the position and draw the image
        x = self.col * CELL_SIZE + (CELL_SIZE // 2) - (self.image.get_width() // 2)
        y = self.row * CELL_SIZE + (CELL_SIZE // 2) - (self.image.get_height() // 2)
        screen.blit(self.image, (x, y))
