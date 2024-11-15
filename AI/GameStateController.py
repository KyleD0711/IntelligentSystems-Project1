from Sprites.Pellet import Pellet
from Sprites.Pacman import Pacman
import numpy as np
class GameStateController:
    def __init__(self, gameBoard, pellets):
        self.gameBoard = gameBoard
        self.num_pellets = len(pellets)
        self.pacman = Pacman(13, 23)
        self.pellets = pellets

    def isGameOver(self):
        return self.num_pellets == 0 or not self.pellets or len(self.pellets) == 0

    def handlePelletPacmanCollision(self):
        print(self.pacman.col, self.pacman.row)
        pellets_to_remove = []
        for pellet in self.pellets:
            if int(self.pacman.col) == int(pellet.col) and int(self.pacman.row) == int(pellet.row):
                pellets_to_remove.append(pellet)
                self.num_pellets -= 1
        for pellet in pellets_to_remove:
            self.pellets.remove(pellet)

    def draw(self, screen):
        self.pacman.draw(screen)
        for pellet in self.pellets:
            pellet.draw(screen)

    def moveEntities(self):
        self.movePacman()

    def movePacman(self):
        self.pacman.move(self.gameBoard, self.pellets)
        self.handlePelletPacmanCollision()