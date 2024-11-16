import pygame
import os
from AI.BrainGhost import BrainGhost
from AI.MazeTree import TreeNode, generate_tree, get_directions_to_cell
from Sprites.Direction import Direction

CELL_SIZE = int(os.getenv("CELL_SIZE", 24))

# Define the Ghost class
class Ghost(pygame.sprite.Sprite):
    def __init__(self, col, row, image_path="ghost.png"):
        super().__init__()
        self.col = col
        self.row = row
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (CELL_SIZE, CELL_SIZE))
        self.brain = BrainGhost()  # Create Brain for Ghost
        self.moves = []  # Store precomputed moves

    def getPosition(self):
        return (self.col, self.row)

    def draw(self, screen):
        x = self.col * CELL_SIZE + (CELL_SIZE // 2) - (self.image.get_width() // 2)
        y = self.row * CELL_SIZE + (CELL_SIZE // 2) - (self.image.get_height() // 2)
        screen.blit(self.image, (x, y))

    def move(self, gameBoard, pacman_coords):
        if not self.moves:
            moveTree = generate_tree(gameBoard, (self.row, self.col))
            self.moves = get_directions_to_cell(moveTree, TreeNode(pacman_coords[1], pacman_coords[0]))

        if self.moves:
            next_move = self.moves.pop(0)
            next_row, next_col, direction = next_move

            # Check the new position and update the ghost's row and column
            if direction == Direction.UP:
                self.direction = 90
                if next_row >= 0:  # Ensure the new row is within bounds
                    self.row = next_row
            elif direction == Direction.DOWN:
                self.direction = 270
                if next_row < len(gameBoard):  # Ensure the new row is within bounds
                    self.row = next_row
            elif direction == Direction.LEFT:
                self.direction = 180
                if next_col >= 0:  # Ensure the new column is within bounds
                    self.col = next_col
            elif direction == Direction.RIGHT:
                self.direction = 0
                if next_col < len(gameBoard[0]):  # Ensure the new column is within bounds
                    self.col = next_col
