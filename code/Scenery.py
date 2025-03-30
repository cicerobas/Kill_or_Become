import pygame.image
from pygame import Surface

from code.Constants import WIN_WIDTH


class Layer:
    def __init__(self, image, speed, pos_x):
        self.image = image
        self.speed = speed
        self.pos_x = pos_x


class Scenery:
    def __init__(self):
        self.layers: list[Layer] = []
        for i in range(0, 5):
            self.layers.append(
                Layer(pygame.image.load(f"assets/sprites/World/World_BG_{i}.png").convert_alpha(), i * 0.075, 0))
        self.layers.append(Layer(pygame.image.load(f"assets/sprites/World/Road.png").convert_alpha(), 0.6, 0))

    def update(self, window: Surface, p_speed: int, direction: str):
        scroll = p_speed if direction == "R" else -p_speed
        for layer in self.layers:
            layer.pos_x -= scroll * layer.speed
            if layer.pos_x <= -WIN_WIDTH:
                layer.pos_x += WIN_WIDTH
            elif layer.pos_x >= 0:
                layer.pos_x -= WIN_WIDTH
            window.blit(layer.image, (layer.pos_x, 0))
            window.blit(layer.image, (layer.pos_x + WIN_WIDTH, 0))

    def draw(self, window: Surface):
        for layer in self.layers:
            window.blit(layer.image, (layer.pos_x, 0))
            window.blit(layer.image, (WIN_WIDTH, 0))
