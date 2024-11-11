from .Cell import Cell
from Sprites.Pellet import Pellet
from Sprites.Pacman import Pacman
from Sprites.Direction import Direction
import csv

class Maze:
    def __init__(self):
        self.rows: [Cell] = []
        self.currentPos = (0,0)
        self.score = 0
        self.num_pellets = 0

        with open('Environment/MazeStructure.csv', newline='') as mazeStructure:
            mazeCSV = csv.reader(mazeStructure, delimiter=",")

            rowIndex = 0

            for row in mazeCSV:

                colIndex = 0

                cellRow = []

                for cell in row:

                    type = "Empty"
                    cellSprite = None

                    if cell == "1":
                        type = "Wall"
                    elif cell == "0":
                        cellSprite = Pellet(rowIndex, colIndex)
                        self.num_pellets += 1

                    newCell = Cell(rowIndex, colIndex, type, cellSprite)
                    cellRow.append(newCell)

                    colIndex += 1

                self.rows.append(cellRow)
                rowIndex += 1
            self.pacman = Pacman(13, 23)
            self.rows[13][23].sprite = self.pacman

    def draw(self, screen):
        for rowIndex, row in enumerate(self.rows):
            for colIndex, cell in enumerate(row):
                cell.draw(screen)

    def getSurroundingCells(self, row, col):
        currentX = col
        currentY = row
        max_cols = len(self.rows[0])

        if currentY == 14:
            # Apply wrap-around behavior in row 15 (index 14)
            cells = [
                self.rows[currentY - 1][currentX],  # Cell above
                self.rows[currentY][(currentX + 1) % max_cols],  # Wrap to right edge if necessary
                self.rows[currentY + 1][currentX],  # Cell below
                self.rows[currentY][(currentX - 1) % max_cols]  # Wrap to left edge if necessary
            ]
        else:
            # Standard behavior for rows other than 15
            cells = [
                self.rows[currentY - 1][currentX],     # Cell above
                self.rows[currentY][currentX + 1],     # Cell to the right
                self.rows[currentY + 1][currentX],     # Cell below
                self.rows[currentY][currentX - 1]      # Cell to the left
            ]

        return cells

    def getCell(self, col, row) -> Cell:
        return self.rows[row][col]

    def movePacman(self, direction):
        self.pacman.move(direction)
        if type(self.rows[self.pacman.row][self.pacman.col].sprite) == Pellet:
            self.num_pellets -= 1

        self.rows[self.pacman.row][self.pacman.col].sprite = self.pacman




            



            

