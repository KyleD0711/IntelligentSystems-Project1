from AI.Graph import Graph
from Sprites.Direction import path_to_directions


class BrainGhost:
    """
    The BrainGhost class handles the AI logic for determining a ghost's movements
    based on the position of Pac-Man and the ghost's current location.

    Attributes:
        moves (list[str]): A list of directions ('UP', 'DOWN', 'LEFT', 'RIGHT') for the ghost to follow.
        gameBoard (Graph): A graph representation of the maze used for pathfinding.

    Methods:
        getNextMove(pacman, ghost): Determines the next move for the ghost.
        findMovesToPacman(pacman, ghost): Finds the path and translates it into a list of directions to reach Pac-Man.
    """

    def __init__(self, gameBoard: Graph):
        """
        Initializes the BrainGhost instance.

        Args:
            gameBoard (Graph): The graph representation of the maze used for pathfinding.
        """
        self.moves = []  # A list of precomputed moves for the ghost
        self.gameBoard = gameBoard  # Graph representation of the maze

    def getNextMove(self, pacman, ghost):
        """
        Determines the next move for the ghost. If no moves are available,
        computes a new path to Pac-Man.

        Args:
            pacman (tuple[int, int]): Pac-Man's current position (row, col).
            ghost (tuple[int, int]): The ghost's current position (row, col).

        Returns:
            str or None: The next move direction ('UP', 'DOWN', 'LEFT', 'RIGHT')
                         or None if no valid move exists.
        """
        # If no moves are precomputed, calculate a new path
        if not self.moves or len(self.moves) == 0:
            self.moves = self.findMovesToPacman(pacman, ghost)

        # Pop the next move from the list and return it
        if self.moves:
            move = self.moves.pop(0)
            return move  # Return the next move direction

        # Return None if no moves are available
        return None

    def findMovesToPacman(self, pacman, ghost):
        """
        Finds the path to Pac-Man and translates it into a list of directions.

        Args:
            pacman (tuple[int, int]): Pac-Man's current position (row, col).
            ghost (tuple[int, int]): The ghost's current position (row, col).

        Returns:
            list[str]: A list of directions ('UP', 'DOWN', 'LEFT', 'RIGHT') to reach Pac-Man.
        """
        # Find the shortest path from the ghost to Pac-Man
        path = self.gameBoard.shortest_path(ghost, pacman)

        # Translate the path into a list of movement directions
        return path_to_directions(path)
