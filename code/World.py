import random

import pygame
from pygame import Surface

from code.Constants import EVENT_ZOMBIE_SPAWN, SPAWN_TIME, ZOMBIES_SPEED
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.HUD import HUD
from code.Scenery import Scenery
from code.Score import Score


class World:
    def __init__(self, window: Surface):
        self.window = window
        self.scenery = Scenery()
        self.score_window = Score(self.window)
        self.player = EntityFactory.get_entity("Player")
        self.player_group = pygame.sprite.GroupSingle()
        self.player_group.add(self.player)
        self.zombies_group = pygame.sprite.Group()
        self.shots_group = pygame.sprite.Group()
        self.hud = HUD(self.window)
        self.ambient_sounds = [pygame.mixer.Sound(f"./assets/sounds/Z{i}.mp3") for i in range(1, 4)]
        pygame.time.set_timer(EVENT_ZOMBIE_SPAWN, SPAWN_TIME)

    def run(self):
        self.play_ambient_sounds(True)
        running = True
        clock = pygame.time.Clock()
        self.scenery.draw(self.window)
        while running:
            if self.player.dead:
                self.play_ambient_sounds(False)
                self.score_window.game_over(self.player.score)
            for zombie in self.zombies_group:
                if zombie.health <= 0:
                    zombie.update_action(4)
                elif zombie.attacking:
                    zombie.update_action(2)
                    if zombie.attacked:
                        EntityMediator.verify_melee_attack(zombie, self.player)
                elif zombie.moving:
                    zombie.update_action(1)
                else:
                    zombie.update_action(0)

            if self.player.health <= 0:
                self.player.update_action(7)
                self.player.dead = True
            elif self.player.shooting:
                self.player.update_action(5)
            elif self.player.reloading:
                self.player.update_action(6)
            elif self.player.attacking:
                self.player.update_action(self.player.attack_option)
                if self.player.attacked:
                    self.player.attacking = False
                    for zombie in self.zombies_group:
                        EntityMediator.verify_melee_attack(self.player, zombie)
            elif self.player.moving:
                is_player_running = pygame.key.get_mods() & pygame.KMOD_SHIFT
                self.player.update_action(2 if is_player_running else 1)
            else:
                self.player.update_action(0)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.play_ambient_sounds(False)
                    running = False
                if event.type == EVENT_ZOMBIE_SPAWN:
                    self.spawn_zombie()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.player.set_moving(True, "L")
                    if event.key == pygame.K_d:
                        self.player.set_moving(True, "R")
                    if event.key == pygame.K_q:
                        if not self.player.attacking:
                            self.player.attack()
                    if event.key == pygame.K_r:
                        self.player.reload()
                    if event.key == pygame.K_SPACE:
                        if self.player.gun_ammo >= 1 and not self.player.shooting:
                            self.player.shot()
                            if len(self.shots_group) <= 0:
                                shot = EntityFactory.get_entity("Shot")
                                shot.direction = "R" if self.player.direction == "R" else "L"
                                self.shots_group.add(shot)
                        else:
                            self.player.reload()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.player.set_moving(False)
                    if event.key == pygame.K_d:
                        self.player.set_moving(False)

            self.scenery.update(self.window, self.player.speed, self.player.direction)
            self.player_group.draw(self.window)
            self.player_group.update()
            self.zombies_group.draw(self.window)
            self.zombies_group.update()
            self.update_zombies()
            self.shots_group.draw(self.window)
            self.shots_group.update()
            for shot in self.shots_group:
                EntityMediator.verify_shot_collision(shot, self.zombies_group.sprites())
            EntityMediator.verify_kill(self.player, self.zombies_group.sprites())

            self.hud.draw(self.player.health, self.player.gun_ammo, self.player.ammo, self.player.score)
            pygame.display.update()
            clock.tick(60)

    def spawn_zombie(self):
        name_choice = random.choice(['Zombie_1', 'Zombie_2', 'Zombie_3', 'Zombie_4'])
        zombie = EntityFactory.get_entity(name_choice)
        self.zombies_group.add(zombie)
        zombie.update_action(1)

    def update_zombies(self):
        for zombie in self.zombies_group:
            if self.player.moving:
                if self.player.direction == "R":
                    zombie.rect.centerx -= self.player.speed
                else:
                    zombie.rect.centerx += self.player.speed

            if zombie.alive:
                zombie.moving = not EntityMediator.verify_entities_collision(zombie, self.player)
                if zombie.moving:
                    if zombie.direction == "R":
                        zombie.rect.centerx += ZOMBIES_SPEED[zombie.name]
                    else:
                        zombie.rect.centerx -= ZOMBIES_SPEED[zombie.name]

                elif not self.player.dead:
                    if self.player.direction != zombie.direction:
                        self.player.set_moving(False)
                    zombie.attack()

    def play_ambient_sounds(self, play: bool):
        for sound in self.ambient_sounds:
            if play:
                sound.play(-1)
            else:
                sound.stop()
