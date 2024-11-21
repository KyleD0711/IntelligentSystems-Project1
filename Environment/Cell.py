import pygame


class Cell:
    def __init__(self, row, col, type, cost=0):
        self.row = row
        self.col = col
        self.type = type
        self.cost = cost