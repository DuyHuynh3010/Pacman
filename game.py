import pygame
from pacman import Pacman
from wall import Wall
from dot import Dot
from ghost_class import Ghost

BLACK = (0, 0, 0)

class Game:
    def __init__(self):
        pygame.init()
        self.width, self.height = 600, 600
        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Pacman OOP - Complete")
        self.clock = pygame.time.Clock()
        self.running = True

        self.pacman = Pacman(50, 50)
        self.walls = [
            Wall(100, 100, 400, 20),
            Wall(100, 200, 20, 300),
            Wall(200, 300, 300, 20)
        ]
        self.dots = [
            Dot(150, 50),
            Dot(300, 150),
            Dot(450, 400)
        ]
        self.ghosts = [
            Ghost(200, 200, (255, 0, 0)),
            Ghost(400, 300, (0, 255, 0)),
        ]
        self.score = 0

    def handle_keys(self):
        dx, dy = 0, 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: dx = -self.pacman.speed
        if keys[pygame.K_RIGHT]: dx = self.pacman.speed
        if keys[pygame.K_UP]: dy = -self.pacman.speed
        if keys[pygame.K_DOWN]: dy = self.pacman.speed
        self.pacman.move(dx, dy, self.walls)

    def update(self):
        self.handle_keys()
        self.check_dot_collision()
        self.move_ghosts()

    def check_dot_collision(self):
        pacman_rect = self.pacman.get_rect()
        for dot in self.dots[:]:
            if pacman_rect.colliderect(dot.rect):
                self.dots.remove(dot)
                self.score += 10

    def move_ghosts(self):
        for ghost in self.ghosts:
            ghost.move(self.pacman.get_rect(), self.walls)

    def draw(self):
        self.win.fill(BLACK)
        for wall in self.walls:
            wall.draw(self.win)
        for dot in self.dots:
            dot.draw(self.win)
        for ghost in self.ghosts:
            ghost.draw(self.win)
        self.pacman.draw(self.win)

        # Draw score
        font = pygame.font.SysFont("Arial", 24)
        score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.win.blit(score_text, (10, 10))

        pygame.display.update()

    def check_ghost_collision(self):
        pacman_rect = self.pacman.get_rect()
        for ghost in self.ghosts:
            if pacman_rect.colliderect(ghost.get_rect()):
                return True
        return False

    def run(self):
        while self.running:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.update()

            # Check if Pacman collided with Ghost
            if self.check_ghost_collision():
                self.running = False

            self.draw()

            if not self.dots:
                print("You Win!")
                self.running = False

        pygame.quit()