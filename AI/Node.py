from Environment.Cell import Cell
from Environment.Maze import Maze
class Node:
    def __init__(self, maze: Maze, visited: [Cell], position: (int, int)):
        surrounding_cells = maze.getSurroundingCells(position.x, position.y)
        self.children = []
        self.position = position
        for cell in surrounding_cells:
            if cell not in visited and cell.type == "Empty":
                new_position = maze.getCell(cell.col, cell.row)
                visited.append(cell)
                self.children.append(Node(maze, visited, new_position))

    # def getPath(self) -> [Direction]: