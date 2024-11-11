import pygame
import os

CELL_SIZE = os.getenv("CELL_SIZE", 24)
class Pellet(pygame.sprite.Sprite):
    def __init__(self, row, col, size=5, color=(255, 255, 255)):
        super().__init__()
        self.row = col  # X position of the pellet
        self.col = row  # Y position of the pellet
        self.size = size  # Radius of the pellet
        self.color = color  # Color of the pellet (white by default)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.row * CELL_SIZE + (CELL_SIZE / 2), self.col * CELL_SIZE + (CELL_SIZE / 2)), self.size)