from abc import ABC, abstractmethod

import pygame
from pygame import Surface

from code.Animations import Animations
from code.Constants import DAMAGE


class Entity(ABC, pygame.sprite.Sprite):
    def __init__(self, name: str, position: tuple[int, int]):
        super().__init__()
        self.name = name
        self.speed = 0
        self.health = 0
        self.damage = DAMAGE[self.name]
        self.direction = self.direction = "R" if position[0] <= 480 else "L"
        self.animations = Animations(name)
        self.animation_frames: list[Surface] = self.animations.get_frames('Idle', self.direction == "L")
        self.current_frame = 0
        self.alive = True
        self.dead = False
        self.death_time = 0
        self.moving = False
        self.attacking = False
        self.attacked = False
        self.image = self.animation_frames[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.midbottom = position

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def attack(self):
        pass
