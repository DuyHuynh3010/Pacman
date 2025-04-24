import pygame

class Ghost:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, 20, 20)  # Thêm thuộc tính rect

    def move(self, pacman_rect, walls):
        # Logic di chuyển của Ghost, kiểm tra va chạm với tường trước khi di chuyển

        # Di chuyển theo hướng x
        if pacman_rect.x > self.rect.x:
            new_rect = self.rect.move(1, 0)  # Dự tính di chuyển 1 pixel sang phải
            if not any(new_rect.colliderect(wall.rect) for wall in walls):  # Kiểm tra va chạm với tường
                self.rect.x += 1  # Chỉ di chuyển nếu không va chạm
        elif pacman_rect.x < self.rect.x:
            new_rect = self.rect.move(-1, 0)  # Dự tính di chuyển 1 pixel sang trái
            if not any(new_rect.colliderect(wall.rect) for wall in walls):
                self.rect.x -= 1

        # Di chuyển theo hướng y
        if pacman_rect.y > self.rect.y:
            new_rect = self.rect.move(0, 1)  # Dự tính di chuyển 1 pixel xuống dưới
            if not any(new_rect.colliderect(wall.rect) for wall in walls):
                self.rect.y += 1
        elif pacman_rect.y < self.rect.y:
            new_rect = self.rect.move(0, -1)  # Dự tính di chuyển 1 pixel lên trên
            if not any(new_rect.colliderect(wall.rect) for wall in walls):
                self.rect.y -= 1

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)  # Vẽ Ghost

    def get_rect(self):  # Thêm phương thức get_rect() để truy xuất rect của Ghost
        return self.rect