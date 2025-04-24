import pygame

class Pacman:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5
        self.rect = pygame.Rect(self.x, self.y, 20, 20)

    def move(self, dx, dy, walls):
        self.rect.x += dx
        self.rect.y += dy


        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0:
                    self.rect.right = wall.rect.left
                if dx < 0:
                    self.rect.left = wall.rect.right
                if dy > 0:
                    self.rect.bottom = wall.rect.top
                if dy < 0:
                    self.rect.top = wall.rect.bottom

    def draw(self, win):
        pygame.draw.rect(win, (255, 255, 0), self.rect)

    def get_rect(self):
        return self.rect