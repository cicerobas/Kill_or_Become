import pygame

from code.Constants import ANIMATION_COOLDOWN, INITIAL_AMMO, WEAPON_CAPACITY, PLAYER_WALK_SPEED, PLAYER_RUN_SPEED, \
    PLAYER_MAX_HEALTH
from code.Entity import Entity


class Player(Entity):

    def __init__(self, name: str, position: tuple[int, int]):
        super().__init__(name, position)
        self.health = PLAYER_MAX_HEALTH
        self.action = 0
        self.update_time = pygame.time.get_ticks()
        self.animation_options = {
            0: "Idle",
            1: "Walk",
            2: "Run",
            3: "Attack_1",
            4: "Attack_2",
            5: "Shot",
            6: "Reload",
            7: "Dead"
        }
        self.attack_option = 3
        self.reloading = False
        self.shooting = False
        self.running = False
        self.ammo = INITIAL_AMMO
        self.gun_ammo = WEAPON_CAPACITY
        self.score = 0
        self.shot_sound = pygame.mixer.Sound("./assets/sounds/Shot.mp3")
        self.reload_sound = pygame.mixer.Sound("./assets/sounds/Reload.mp3")

    def update(self):
        if self.alive:
            if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
                self.update_time = pygame.time.get_ticks()
                self.current_frame += 1

            if self.current_frame >= len(self.animation_frames):
                self.current_frame = 0

                if self.shooting or self.reloading:
                    self.update_ammo(self.shooting, self.reloading)

                if self.health <= 0:
                    self.current_frame = -1
                    self.alive = False
                    self.death_time = pygame.time.get_ticks()

                self.attacked = True
                self.reloading = False
                self.shooting = False

            self.image = self.animation_frames[self.current_frame]
        else:
            if pygame.time.get_ticks() - self.death_time > 2000:
                self.kill()

    def update_action(self, new_action):
        if new_action != self.action:
            match new_action:
                case 1:
                    self.speed = PLAYER_WALK_SPEED
                case 2:
                    self.speed = PLAYER_RUN_SPEED
                    self.running = True
                case 5:
                    self.shot_sound.play()
                case 6:
                    self.reload_sound.play()
                case _:
                    self.speed = 0
                    self.running = False

            self.action = new_action
            self.animation_frames = self.animations.get_frames(self.animation_options[self.action],
                                                               self.direction == "L")
            self.current_frame = 0
            self.update_time = pygame.time.get_ticks()

    def set_moving(self, is_moving: bool, direction: str = ""):
        if is_moving:
            self.speed = PLAYER_RUN_SPEED if self.running else PLAYER_WALK_SPEED
            self.moving = True
            self.direction = direction
        else:
            self.moving = False

    def attack(self):
        self.attacked = False
        self.attacking = True
        self.attack_option = 3 if self.attack_option == 4 else 4

    def shot(self):
        self.shooting = True

    def reload(self):
        if self.ammo >= 1 and self.gun_ammo != WEAPON_CAPACITY:
            self.reloading = True

    def update_ammo(self, shot: bool, reload: bool):
        if shot:
            self.gun_ammo -= 1
        if reload:
            to_reload = WEAPON_CAPACITY - self.gun_ammo
            if to_reload <= self.ammo:
                self.ammo -= to_reload
                self.gun_ammo = WEAPON_CAPACITY
            else:
                self.gun_ammo = self.ammo
                self.ammo = 0
