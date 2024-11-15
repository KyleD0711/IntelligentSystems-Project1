from AI.MazeTree import get_directions_to_cell, generate_tree

class Brain:
    def __init__(self):
        self.moves = []
    def getNextMove(self, gameBoard, pellets, pacman_coords):
        if not self.moves or len(self.moves) == 0:
            closestPellet = self.findClosestPellet(pacman_coords, pellets)
            if closestPellet is None:
                return None
            self.moves = self.findMovesToPellet(gameBoard, pacman_coords, closestPellet)
        if self.moves:
            move = self.moves.pop(0)
            return move[2]
        else:
            return None

    def findClosestPellet(self, pacman_coords, pellets):
        if not pellets:
            return None
        closestPellet = pellets[0]
        closestDistance = self.getDistance(pellets[0], pacman_coords)
        for pellet in pellets:
            distance = self.getDistance(pellet, pacman_coords)
            if distance < closestDistance:
                closestDistance = distance
                closestPellet = pellet
        return closestPellet

    def findMovesToPellet(self, gameBoard, coords, pellet):
        moveTree = generate_tree(gameBoard, coords)
        return get_directions_to_cell(moveTree, pellet)

    def getDistance(self, pellet, pacman_coords):
        return self.heuristic(pellet.col, pellet.row, pacman_coords[0], pacman_coords[1])

    def heuristic(self, x1: int, y1: int, x2: int, y2: int) -> int:
        return abs(x1 - x2) + abs(y1 - y2)