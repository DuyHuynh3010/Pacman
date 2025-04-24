import pygame

class Dot:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 10, 10)

    def draw(self, win):
        pygame.draw.ellipse(win, (255, 255, 255), self.rect)
