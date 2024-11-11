from turtledemo.penrose import start

from AI.Node import Node
from Environment.Maze import Maze
class MazeTree:
    def __init__(self, maze: Maze):
        starting_position = maze.pacman.getPosition()

        starting_cell = maze.getCell(starting_position.x, starting_position.y)
        visited = [starting_cell]
        self.root = Node(maze, visited, starting_position)
