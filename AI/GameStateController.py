from Sprites.Ghost import Ghost
from Sprites.Pacman import Pacman
from Sprites.Score import Score
from AI.Graph import Graph

class GameStateController:
    """
    The GameStateController class manages the game logic, including interactions
    between Pac-Man, ghosts, and pellets, as well as the game's overall state.

    Attributes:
        gameBoard (Graph): A graph representation of the maze for pathfinding.
        num_pellets (int): The total number of pellets in the game.
        pacman (Pacman): The Pac-Man character.
        pellets (list[Pellet]): List of Pellet objects remaining in the game.
        pellets_tuple (list[tuple[int, int]]): List of pellet positions for easy collision detection.
        ghost (Ghost): The ghost character.
        score (Score): The score tracker for the game.

    Methods:
        isGameOver(): Determines if the game is over (win or loss condition).
        handlePelletPacmanCollision(): Handles collisions between Pac-Man and pellets, updating the score.
        draw(screen): Draws all game entities (Pac-Man, ghost, pellets, score) on the screen.
        moveEntities(): Moves Pac-Man and the ghost, handling interactions.
        movePacman(): Moves Pac-Man and checks for pellet collisions.
        moveGhost(): Moves the ghost based on Pac-Man's position.
    """

    def __init__(self, gameBoard, pellets, algorithm=None):
        """
        Initializes the GameStateController with the game board, pellets, and AI algorithm.

        Args:
            gameBoard (list[list[Cell]]): 2D grid representing the maze.
            pellets (list[Pellet]): List of Pellet objects in the maze.
            algorithm (str, optional): Algorithm used for ghost AI. Defaults to None.
        """
        self.gameBoard = Graph(gameBoard, algorithm=algorithm)  # Graph for pathfinding
        self.num_pellets = len(pellets)  # Total number of pellets
        self.pacman = Pacman(13, 23, 48, self.gameBoard)  # Initialize Pac-Man at default position
        self.pellets = pellets  # List of Pellet objects
        self.pellets_tuple = [(pellet.row, pellet.col) for pellet in pellets]  # Pellet positions for collision
        self.ghost = Ghost(6, 5, 48, self.gameBoard)  # Initialize ghost at default position
        self.score = Score()  # Initialize the score tracker

    def isGameOver(self):
        """
        Checks if the game is over.

        Returns:
            bool: True if the game is over (all pellets collected or Pac-Man caught by the ghost), False otherwise.
        """
        pacman_pos = (self.pacman.row, self.pacman.col)
        ghost_pos = (self.ghost.row, self.ghost.col)
        return self.num_pellets == 0 or not self.pellets or len(self.pellets) == 0 or pacman_pos == ghost_pos

    def handlePelletPacmanCollision(self):
        """
        Handles collisions between Pac-Man and pellets. Updates the score and removes collected pellets.
        """
        self.score.add_score(50)  # Add points for each pellet collected
        pellets_to_remove = []

        for pellet in self.pellets:
            if int(self.pacman.col) == int(pellet.col) and int(self.pacman.row) == int(pellet.row):
                pellets_to_remove.append(pellet)
                self.num_pellets -= 1  # Decrement pellet count

        for pellet in pellets_to_remove:
            self.pellets.remove(pellet)  # Remove pellet from the list
            self.pellets_tuple.remove((pellet.row, pellet.col))  # Remove pellet position

    def draw(self, screen):
        """
        Draws all game entities on the screen.

        Args:
            screen (pygame.Surface): The surface to draw on.
        """
        self.pacman.draw(screen)  # Draw Pac-Man
        self.score.draw(screen)  # Draw the score
        for pellet in self.pellets:
            pellet.draw(screen)  # Draw pellets
        self.ghost.draw(screen)  # Draw the ghost

    def moveEntities(self):
        """
        Moves all game entities (Pac-Man and ghost) and handles interactions.
        """
        self.movePacman()
        self.moveGhost()

    def movePacman(self):
        """
        Moves Pac-Man and checks for collisions with pellets.
        """
        self.pacman.move(self.pellets_tuple, self.ghost.getPosition())  # Move Pac-Man
        self.handlePelletPacmanCollision()  # Check for pellet collisions

    def moveGhost(self):
        """
        Moves the ghost based on Pac-Man's position.
        """
        self.ghost.move(self.pacman.getPosition())  # Move the ghost
