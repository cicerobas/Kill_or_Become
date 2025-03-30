import random

from code.Constants import PLAYER_X_POSITION, ZOMBIES_SPAWN_ZONES
from code.Player import Player
from code.Shot import Shot
from code.Zombie import Zombie


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        if entity_name == "Player":
            return Player(entity_name, (PLAYER_X_POSITION, 465))
        elif entity_name == "Shot":
            return Shot(entity_name)
        else:
            spawn_zone = random.choice(ZOMBIES_SPAWN_ZONES)
            return Zombie(entity_name, (random.randint(spawn_zone[0], spawn_zone[1]), 465))
