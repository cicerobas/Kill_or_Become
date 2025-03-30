import pygame

from code.Constants import DAMAGE, WIN_WIDTH, HITBOX_FACTOR


class Shot(pygame.sprite.Sprite):
    def __init__(self, name: str):
        super().__init__()
        self.name = name
        self.speed = 50
        self.damage = DAMAGE[self.name]
        self.direction = "R"
        self.image = pygame.image.load("./assets/sprites/Shot/Shot.png").convert_alpha()
        self.rect = self.image.get_rect(center=(WIN_WIDTH / 2 + HITBOX_FACTOR, 340))

    def update(self):
        if self.direction == "R":
            self.rect.x += self.speed
        else:
            self.rect.x -= self.speed

        if self.rect.x < 0 or self.rect.x > WIN_WIDTH:
            self.kill()
