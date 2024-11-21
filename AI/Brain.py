from Sprites.Direction import path_to_directions
from AI.Graph import Graph
class Brain:
    def __init__(self, gameBoard : Graph):
        self.current_goal = None
        self.gameBoard = gameBoard

    def getNextMove(self, pellets, pacman, ghost):
        self.current_goal = self.findClosestPellet(pacman, pellets, ghost)
        if self.current_goal is None:
            return None
        goal = (self.current_goal[0], self.current_goal[1])
        return self.findMovesToPellet(pacman, goal, ghost)

    def findClosestPellet(self, pacman, pellets, ghost):
        if not pellets:
            return None
        closestPellet = pellets[0]
        closestDistance = self.getDistance(pellets[0], pacman, ghost)
        for pellet in pellets:
            distance = self.getDistance(pellet, pacman, ghost)
            if distance < closestDistance:
                closestDistance = distance
                closestPellet = pellet
        return closestPellet

    def findMovesToPellet(self, pacman, pellet, ghost):
        path = self.gameBoard.shortest_path(pacman, pellet, ghost)
        print(path)
        return path_to_directions(path)[0]

    def getDistance(self, pellet, pacman, ghost):
        if pellet[0] == ghost[0] and pellet[1] == ghost[1]:
            return self.heuristic(pellet[0], pellet[1], pacman[0], pacman[1]) + 5000
        else:
            return self.heuristic(pellet[0], pellet[1], pacman[0], pacman[1]) + 50 * (1 / self.heuristic(pellet[0], pellet[1], ghost[0], ghost[1]))

    def heuristic(self, x1: int, y1: int, x2: int, y2: int) -> int:
        return self.gameBoard.getDistanceFromStartToTarget((x1, y1), (x2, y2))