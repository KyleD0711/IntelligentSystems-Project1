from .Cell import Cell
from Sprites.Pellet import Pellet
from AI.GameStateController import GameStateController
import csv
import os

class Maze:
    # GameStateController
    # Cells
    # Pellets
    # Pacman
    # Ghosts
    # Total Num of Pellets
    # Total Score

    # Move entities
    #   Move Pacman
    #   Handle Pellet Pacman collision
    #   Handle Ghost Movement
    def __init__(self, yOffset, algorithm):
        self.gameBoard: [Cell] = []
        self.yOffset = yOffset
        pellets = []

        PACMAN_START_ROW = os.getenv("PACMAN_START_ROW", 23)
        PACMAN_START_COL = os.getenv("PACMAN_START_COL",13)


        with open('Environment/MazeStructure.csv', newline='') as mazeStructure:
            mazeCSV = csv.reader(mazeStructure, delimiter=",")

            rowIndex = 0

            for row in mazeCSV:
                colIndex = 0

                cellRow = []

                for cell in row:
                    type = "Empty"

                    if cell == "1":
                        type = "Wall"
                    elif cell == "0":
                        if rowIndex != PACMAN_START_ROW or colIndex != PACMAN_START_COL:
                            pellets.append(Pellet(rowIndex, colIndex, self.yOffset))

                    newCell = Cell(rowIndex, colIndex, type)
                    cellRow.append(newCell)

                    colIndex += 1

                self.gameBoard.append(cellRow)
                rowIndex += 1

        self.gameStateController = GameStateController(self.gameBoard, pellets, algorithm)

    def moveEntities(self):
        self.gameStateController.moveEntities()

    def isOver(self):
        return self.gameStateController.isGameOver()

    def draw(self, screen):
        self.gameStateController.draw(screen)