from AI.Graph import Graph
from Sprites.Direction import path_to_directions
class BrainGhost:
    def __init__(self, gameBoard: Graph):
        self.moves = []
        self.gameBoard = gameBoard

    def getNextMove(self, pacman, ghost):
        if not self.moves or len(self.moves) == 0:
            self.moves = self.findMovesToPacman(pacman, ghost)
        if self.moves:
            move = self.moves.pop(0)
            return move  # Return direction (UP, DOWN, LEFT, RIGHT)
        return None

    def findMovesToPacman(self, pacman, ghost):
        path = self.gameBoard.shortest_path(ghost, pacman)
        return path_to_directions(path)