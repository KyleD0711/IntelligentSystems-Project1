import pygame


class Cell:
    def __init__(self, row, col, type, sprite: pygame.sprite.Sprite = None):
        self.row = row
        self.col = col
        self.type = type