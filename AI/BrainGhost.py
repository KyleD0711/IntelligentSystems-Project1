from AI.MazeTree import get_directions_to_cell, generate_tree
from AI.MazeTree import TreeNode

class BrainGhost:
    def __init__(self):
        self.moves = []

    def getNextMove(self, gameBoard, pacman_coords, ghost_coords):
        if not self.moves:
            self.moves = self.findMovesToPacman(gameBoard, ghost_coords, pacman_coords)

        if self.moves:
            move = self.moves.pop(0)
            return move[2]  # Return direction (UP, DOWN, LEFT, RIGHT)
        return None

    def findMovesToPacman(self, gameBoard, ghost_coords, pacman_coords):
        moveTree = generate_tree(gameBoard, ghost_coords)
        return get_directions_to_cell(moveTree, TreeNode(pacman_coords[1], pacman_coords[0]))

