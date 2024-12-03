from .Cell import Cell
from Sprites.Pellet import Pellet
from AI.GameStateController import GameStateController
import csv
import os

class Maze:
    """
    The Maze class represents the game board for Pac-Man, including its structure, entities, and logic.

    Attributes:
        gameBoard (list[list[Cell]]): A 2D list of Cell objects representing the game grid.
        yOffset (int): Vertical offset for drawing the maze.
        gameStateController (GameStateController): Manages game state and controls entities like Pac-Man and ghosts.

    Methods:
        moveEntities(): Moves all entities (Pac-Man, ghosts) and handles collisions.
        isOver(): Checks if the game is over.
        draw(screen): Draws the maze, Pac-Man, ghosts, and pellets on the screen.
    """

    def __init__(self, yOffset, algorithm):
        """
        Initializes the Maze instance by loading the maze structure from a CSV file,
        placing pellets, and initializing the game state controller.

        Args:
            yOffset (int): Vertical offset for rendering the maze.
            algorithm (str): The algorithm used by the AI for controlling ghosts.
        """
        self.gameBoard: [Cell] = []  # 2D list representing the maze grid
        self.yOffset = yOffset  # Vertical offset for the maze rendering
        pellets = []  # List to store Pellet objects

        # Define Pac-Man's starting position from environment variables (default row: 23, col: 13)
        PACMAN_START_ROW = int(os.getenv("PACMAN_START_ROW", 23))
        PACMAN_START_COL = int(os.getenv("PACMAN_START_COL", 13))

        # Load the maze structure from a CSV file
        with open('Environment/MazeStructure.csv', newline='') as mazeStructure:
            mazeCSV = csv.reader(mazeStructure, delimiter=",")

            rowIndex = 0
            for row in mazeCSV:
                colIndex = 0
                cellRow = []

                for cell in row:
                    type = "Empty"  # Default cell type is empty

                    if cell == "1":
                        type = "Wall"  # Wall cell
                    elif cell == "0":
                        # Add a pellet if the cell is empty and not the Pac-Man start position
                        if rowIndex != PACMAN_START_ROW or colIndex != PACMAN_START_COL:
                            pellets.append(Pellet(rowIndex, colIndex, self.yOffset))

                    # Create a new Cell object and add it to the current row
                    newCell = Cell(rowIndex, colIndex, type)
                    cellRow.append(newCell)

                    colIndex += 1

                # Append the row of cells to the game board
                self.gameBoard.append(cellRow)
                rowIndex += 1

        # Initialize the GameStateController with the game board, pellets, and AI algorithm
        self.gameStateController = GameStateController(self.gameBoard, pellets, algorithm)

    def moveEntities(self):
        """
        Moves all entities in the maze (Pac-Man, ghosts) and handles collisions.
        """
        self.gameStateController.moveEntities()

    def isOver(self):
        """
        Checks if the game is over.

        Returns:
            bool: True if the game is over, False otherwise.
        """
        return self.gameStateController.isGameOver()

    def draw(self, screen):
        """
        Draws the maze, including walls, pellets, Pac-Man, and ghosts, on the given screen.

        Args:
            screen (pygame.Surface): The surface to draw on.
        """
        self.gameStateController.draw(screen)
