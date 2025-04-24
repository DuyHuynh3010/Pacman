import pygame

class Ghost:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, 20, 20)

    def move(self, pacman_rect, walls):



        if pacman_rect.x > self.rect.x:
            new_rect = self.rect.move(1, 0)
            if not any(new_rect.colliderect(wall.rect) for wall in walls):
                self.rect.x += 1
        elif pacman_rect.x < self.rect.x:
            new_rect = self.rect.move(-1, 0)
            if not any(new_rect.colliderect(wall.rect) for wall in walls):
                self.rect.x -= 1

        # move Y
        if pacman_rect.y > self.rect.y:
            new_rect = self.rect.move(0, 1)
            if not any(new_rect.colliderect(wall.rect) for wall in walls):
                self.rect.y += 1
        elif pacman_rect.y < self.rect.y:
            new_rect = self.rect.move(0, -1)
            if not any(new_rect.colliderect(wall.rect) for wall in walls):
                self.rect.y -= 1

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def get_rect(self):
        return self.rect