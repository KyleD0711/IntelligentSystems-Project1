import pygame
import math
import os
from Sprites.Direction import Direction
from AI.Brain import Brain

CELL_SIZE = os.getenv("CELL_SIZE", 24)
# Define the Pacman class
class Pacman(pygame.sprite.Sprite):
    def __init__(self, col, row, size = 10, color=(255, 255, 0)):
        super().__init__()
        self.col = col  # Pacman's x position
        self.row = row  # Pacman's y position
        self.size = size  # Radius of Pacman
        self.color = color  # Pacman's color (yellow by default)
        self.direction = 0  # Angle of the mouth's direction in degrees (0 is right)
        self.brain = Brain()

    def getPosition(self):
        return (self.col, self.row)

    def draw(self, screen):
        # Define the angle of Pacman's mouth
        mouth_open_angle = 45
        mouth_direction = math.radians(self.direction)  # Convert direction to radians

        # Calculate the starting and ending angles for the mouth
        start_angle = mouth_direction + math.radians(mouth_open_angle)
        end_angle = mouth_direction - math.radians(mouth_open_angle)

        # Draw Pacman's body as an arc
        pygame.draw.arc(screen, self.color,
                        (self.col * CELL_SIZE + (CELL_SIZE / 2) - self.size, self.row * CELL_SIZE + (CELL_SIZE / 2) - self.size, self.size * 2, self.size * 2),
                        start_angle, end_angle, self.size)

    def set_direction(self, angle):
        # Set Pacman's direction based on the angle (in degrees)
        self.direction = angle

    def move(self, gameBoard, pellets):
        direction = self.getNextMove(gameBoard, pellets)

        if direction == Direction.UP:
            self.direction = 90
            self.row -= 1
        elif direction == Direction.DOWN:
            self.direction = 270
            self.row += 1
        elif direction == Direction.LEFT:
            self.direction = 180
            self.col -= 1
        elif direction == Direction.RIGHT:
            self.direction = 0
            self.col += 1

    def getNextMove(self, gameBoard, pellets):
        return self.brain.getNextMove(gameBoard, pellets, self.getPosition())


