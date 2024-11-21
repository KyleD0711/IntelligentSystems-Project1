from Sprites.Ghost import Ghost
from Sprites.Pacman import Pacman
from Sprites.Score import Score
from AI.Graph import Graph
class GameStateController:
    def __init__(self, gameBoard, pellets, algorithm=None):
        self.gameBoard = Graph(gameBoard, algorithm=algorithm)
        self.num_pellets = len(pellets)
        self.pacman = Pacman(13, 23, 48, self.gameBoard)
        self.pellets = pellets
        self.pellets_tuple = []
        for pellet in pellets:
            self.pellets_tuple.append((pellet.row, pellet.col))
        self.ghost = Ghost(6, 5, 48, self.gameBoard)  # A winning game position is col = 6 and row = 5
        self.score = Score()

    def isGameOver(self):
        pacman_pos = (self.pacman.row, self.pacman.col)
        ghost_pos = (self.ghost.row, self.ghost.col)
        return self.num_pellets == 0 or not self.pellets or len(self.pellets) == 0 or pacman_pos == ghost_pos

    def handlePelletPacmanCollision(self):
        pellets_to_remove = []
        for pellet in self.pellets:
            if int(self.pacman.col) == int(pellet.col) and int(self.pacman.row) == int(pellet.row):
                pellets_to_remove.append(pellet)
                self.score.add_score(50)
                self.num_pellets -= 1
        for pellet in pellets_to_remove:
            self.pellets.remove(pellet)
            self.pellets_tuple.remove((pellet.row, pellet.col))

    def draw(self, screen):
        self.pacman.draw(screen)
        self.score.draw(screen)
        for pellet in self.pellets:
            pellet.draw(screen)
        self.ghost.draw(screen)        

    def moveEntities(self):
        self.movePacman()
        self.moveGhost()

    def movePacman(self):
        self.pacman.move(self.pellets_tuple, self.ghost.getPosition())
        self.handlePelletPacmanCollision()

    def moveGhost(self):
        self.ghost.move(self.pacman.getPosition())