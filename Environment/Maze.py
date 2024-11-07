from .Cell import Cell
import csv

class Maze:
    def __init__(self):
        self.rows = []
        self.currentPos = (0,0)

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

                    newCell = Cell(rowIndex, colIndex, type)
                    cellRow.append(newCell)

                    colIndex += 1

                self.rows.append(cellRow)
                rowIndex += 1

    def getSurroundingCells(self):
        currentX = self.currentPos[1]
        currentY = self.currentPos[0]
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


    def movePacman(self, xDiff, yDiff):
        # Input validation
        if (xDiff != 0 and yDiff != 0) or abs(xDiff) > 1 or abs(yDiff) > 1:
            return False

        # Calculate new position
        new_row = self.pacman_position[0] + yDiff
        new_col = self.pacman_position[1] + xDiff
        max_cols = len(self.maze[0])

        # Check for wrap-around behavior in row 15 (index 14)
        if new_row == 14:
            if new_col < 0:  # Moving left off the left edge
                new_col = max_cols - 1  # Wrap to the right edge
            elif new_col >= max_cols:  # Moving right off the right edge
                new_col = 0  # Wrap to the left edge

        # Check if new position is within vertical bounds of the maze
        if new_row < 0 or new_row >= len(self.maze):
            return False  # Out of bounds vertically

        # Check if the new position is a wall
        if self.maze[new_row][new_col] == 1:
            return False  # Cannot move into a wall

        # Update Pac-Man's position
        self.pacman_position = (new_row, new_col)
        return True

            



            

