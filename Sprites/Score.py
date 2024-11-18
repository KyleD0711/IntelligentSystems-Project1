import pygame

# Define the Score class
class Score(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.score = 0;
        self.font = pygame.font.Font('Quinquefive-ALoRM.ttf', 32)

    def add_score(self, addScore):
        self.score += addScore


    def draw(self, screen):
        text = self.font.render('SCORE: ' + str(self.score), True, (255,255,255))

        textRect = text.get_rect()

        background_rect = textRect.inflate(0, 0)

        # Draw the background rectangle
        pygame.draw.rect(screen, (0,0,0), background_rect)

        screen.blit(text, textRect)