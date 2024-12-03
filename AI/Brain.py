from Sprites.Direction import path_to_directions
from AI.Graph import Graph

class Brain:
    """
    The Brain class handles the AI logic for determining Pac-Man's movements
    based on the positions of pellets, Pac-Man, and ghosts.

    Attributes:
        current_goal (tuple[int, int] or None): The current target pellet (row, col) for Pac-Man.
        gameBoard (Graph): A graph representation of the maze used for pathfinding.

    Methods:
        getNextMove(pellets, pacman, ghost): Determines the next move for Pac-Man.
        findClosestPellet(pacman, pellets, ghost): Finds the closest pellet, considering ghost positions.
        findMovesToPellet(pacman, pellet, ghost): Determines the path and translates it into a direction.
        getDistance(pellet, pacman, ghost): Calculates a heuristic distance from Pac-Man to a pellet, considering ghosts.
        heuristic(x1, y1, x2, y2): A heuristic function to estimate the distance between two points.
    """

    def __init__(self, gameBoard: Graph):
        """
        Initializes the Brain instance.

        Args:
            gameBoard (Graph): The graph representation of the maze used for pathfinding.
        """
        self.current_goal = None  # Current target pellet
        self.gameBoard = gameBoard  # Graph representation of the maze

    def getNextMove(self, pellets, pacman, ghost):
        """
        Determines the next move for Pac-Man based on the closest pellet.

        Args:
            pellets (list[tuple[int, int]]): List of pellet positions (row, col).
            pacman (tuple[int, int]): Pac-Man's current position (row, col).
            ghost (tuple[int, int]): The ghost's current position (row, col).

        Returns:
            str or None: The next move direction ('UP', 'DOWN', 'LEFT', 'RIGHT') or None if no goal is found.
        """
        self.current_goal = self.findClosestPellet(pacman, pellets, ghost)
        if self.current_goal is None:
            return None
        goal = (self.current_goal[0], self.current_goal[1])
        return self.findMovesToPellet(pacman, goal, ghost)

    def findClosestPellet(self, pacman, pellets, ghost):
        """
        Finds the closest pellet to Pac-Man, considering the ghost's position.

        Args:
            pacman (tuple[int, int]): Pac-Man's current position (row, col).
            pellets (list[tuple[int, int]]): List of pellet positions (row, col).
            ghost (tuple[int, int]): The ghost's current position (row, col).

        Returns:
            tuple[int, int] or None: The closest pellet's position or None if no pellets remain.
        """
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
        """
        Determines the path to a pellet and translates it into a direction.

        Args:
            pacman (tuple[int, int]): Pac-Man's current position (row, col).
            pellet (tuple[int, int]): The target pellet's position (row, col).
            ghost (tuple[int, int]): The ghost's current position (row, col).

        Returns:
            str: The direction of the next move ('UP', 'DOWN', 'LEFT', 'RIGHT').
        """
        path = self.gameBoard.shortest_path(pacman, pellet, ghost)
        print(path)
        return path_to_directions(path)[0]

    def getDistance(self, pellet, pacman, ghost):
        """
        Calculates a heuristic distance from Pac-Man to a pellet, factoring in ghost proximity.

        Args:
            pellet (tuple[int, int]): Pellet's position (row, col).
            pacman (tuple[int, int]): Pac-Man's position (row, col).
            ghost (tuple[int, int]): Ghost's position (row, col).

        Returns:
            float: The calculated distance.
        """
        if pellet[0] == ghost[0] and pellet[1] == ghost[1]:
            return self.heuristic(pellet[0], pellet[1], pacman[0], pacman[1]) + 5000
        else:
            return self.heuristic(pellet[0], pellet[1], pacman[0], pacman[1]) + \
                   50 * (1 / self.heuristic(pellet[0], pellet[1], ghost[0], ghost[1]))

    def heuristic(self, x1: int, y1: int, x2: int, y2: int) -> int:
        """
        A heuristic function to estimate the distance between two points.

        Args:
            x1 (int): Row of the first point.
            y1 (int): Column of the first point.
            x2 (int): Row of the second point.
            y2 (int): Column of the second point.

        Returns:
            int: The estimated distance between the two points.
        """
        return self.gameBoard.getDistanceFromStartToTarget((x1, y1), (x2, y2))
