import pygame.time

from code.Constants import HITBOX_FACTOR, ZOMBIES_SCORE_VALUE
from code.Entity import Entity
from code.Player import Player
from code.Shot import Shot
from code.Zombie import Zombie


class EntityMediator:
    @staticmethod
    def verify_entities_collision(entity_1, entity_2) -> bool:
        if isinstance(entity_1, Zombie) or isinstance(entity_1, Player):
            if entity_1.direction == "R":
                return entity_1.rect.centerx + HITBOX_FACTOR >= entity_2.rect.centerx - HITBOX_FACTOR
            else:
                return entity_1.rect.centerx - HITBOX_FACTOR <= entity_2.rect.centerx + HITBOX_FACTOR
        elif isinstance(entity_1, Shot):
            if entity_1.direction == "R" and entity_2.direction == "L":
                return entity_1.rect.centerx >= entity_2.rect.centerx - HITBOX_FACTOR
            elif entity_1.direction == "L" and entity_2.direction == "R":
                return entity_1.rect.centerx <= entity_2.rect.centerx + HITBOX_FACTOR
            else:
                return False
        else:
            return False

    @staticmethod
    def verify_melee_attack(attacker: Entity, target: Entity) -> bool:
        if EntityMediator.verify_entities_collision(attacker, target):
            target.health -= attacker.damage
            return True
        return False

    @staticmethod
    def verify_shot_collision(shot: Shot, targets: list[Zombie]):
        for zombie in targets:
            if EntityMediator.verify_entities_collision(shot, zombie):
                zombie.health -= shot.damage
                shot.kill()

    @staticmethod
    def verify_kill(player: Player, zombies: list[Zombie]):
        for zombie in zombies:
            if zombie.health <= 0 and not zombie.dead:
                zombie.dead = True
                player.score += ZOMBIES_SCORE_VALUE[zombie.name]
