import pygame
import os

CELL_SIZE = os.getenv("CELL_SIZE", 24)
class Pellet(pygame.sprite.Sprite):
    def __init__(self, row, col, yOffset, size=5, color=(255, 255, 255)):
        super().__init__()
        self.row = row  # X position of the pellet
        self.col = col  # Y position of the pellet
        self.size = size  # Radius of the pellet
        self.color = color  # Color of the pellet (white by default)
        self.yOffset = yOffset

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.col * CELL_SIZE + (CELL_SIZE / 2), (self.row * CELL_SIZE + (CELL_SIZE / 2)) + self.yOffset), self.size)