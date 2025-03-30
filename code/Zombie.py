import pygame

from code.Constants import ZOMBIES_HEALTH, ZOMBIES_SPEED, ANIMATION_COOLDOWN, WIN_WIDTH
from code.Entity import Entity

class Zombie(Entity):
    def __init__(self, name: str, position: tuple[int, int]):
        super().__init__(name, position)
        self.health = ZOMBIES_HEALTH[name]
        self.speed = ZOMBIES_SPEED[name]
        self.action = 0
        self.update_time = pygame.time.get_ticks()
        self.animation_options = {
            0: "Idle",
            1: "Walk",
            2: "Attack",
            3: "Hurt",
            4: "Dead",
        }

    def update(self):
        if self.alive:
            self.moving = self.action == 1
            self.attacked = False

            if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
                self.update_time = pygame.time.get_ticks()
                self.current_frame += 1

            if self.current_frame >= len(self.animation_frames):
                self.current_frame = 0

                if self.health <= 0:
                    self.current_frame = -1
                    self.alive = False
                    self.death_time = pygame.time.get_ticks()

                self.attacking = False
                self.attacked = True

            self.image = self.animation_frames[self.current_frame]
        else:
            if pygame.time.get_ticks() - self.death_time > 2000:
                self.kill()

    def update_action(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.animation_frames = self.animations.get_frames(self.animation_options[self.action],
                                                               self.direction == "L")
            self.current_frame = 0
            self.update_time = pygame.time.get_ticks()

    def attack(self):
        self.attacking = True
