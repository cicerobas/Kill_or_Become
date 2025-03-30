import pygame

WIN_WIDTH = 960
WIN_HEIGHT = 540

ANIMATION_COOLDOWN = 100
INITIAL_AMMO = 16
WEAPON_CAPACITY = 4

# COLORS
C_BLOOD_RED = (136, 8, 8)
C_WHITE = (255, 255, 255)
C_DARK_GREY = (32, 32, 32)
C_GREEN = (0, 153, 76)

MENU_OPTIONS = ("New Game", "Scores", "Exit")

PLAYER_X_POSITION = WIN_WIDTH / 2
PLAYER_WALK_SPEED = 5
PLAYER_RUN_SPEED = 15
PLAYER_MAX_HEALTH = 100

EVENT_ZOMBIE_SPAWN = pygame.USEREVENT + 1
SPAWN_TIME = 5000

HITBOX_FACTOR = 50

PLAYER_FRAME_DATA = {
    'Attack_1': (128, 128, 6),
    'Attack_2': (128, 128, 3),
    'Dead': (128, 128, 4),
    'Hurt': (128, 128, 2),
    'Idle': (128, 128, 6),
    'Reload': (128, 128, 12),
    'Run': (128, 128, 8),
    'Shot': (128, 128, 12),
    'Walk': (128, 128, 8),
}

DAMAGE = {
    'Player': 25,
    'Shot': 50,
    'Zombie_1': 15,
    'Zombie_2': 5,
    'Zombie_3': 25,
    'Zombie_4': 10,
}
ZOMBIES_SCORE_VALUE = {
    'Zombie_1': 50,
    'Zombie_2': 100,
    'Zombie_3': 150,
    'Zombie_4': 200,
}
ZOMBIES_HEALTH = {
    'Zombie_1': 50,
    'Zombie_2': 75,
    'Zombie_3': 100,
    'Zombie_4': 125,
}
ZOMBIES_SPEED = {
    'Zombie_1': 1.2,
    'Zombie_2': 3,
    'Zombie_3': 1,
    'Zombie_4': 1.4,
}
ZOMBIES_FRAME_DATA = {
    'Zombie_1': {
        'Attack': (128, 128, 5),
        'Dead': (128, 128, 5),
        'Hurt': (128, 128, 4),
        'Idle': (128, 128, 6),
        'Walk': (128, 128, 10),
    },
    'Zombie_2': {
        'Attack': (128, 128, 5),
        'Dead': (128, 128, 5),
        'Hurt': (128, 128, 4),
        'Idle': (128, 128, 6),
        'Walk': (128, 128, 10),
    },
    'Zombie_3': {
        'Attack': (128, 128, 4),
        'Dead': (128, 128, 5),
        'Hurt': (128, 128, 4),
        'Idle': (128, 128, 6),
        'Walk': (128, 128, 10),
    },
    'Zombie_4': {
        'Attack': (128, 128, 10),
        'Dead': (128, 128, 5),
        'Hurt': (128, 128, 4),
        'Idle': (128, 128, 7),
        'Walk': (128, 128, 12),
    },
}
ZOMBIES_SPAWN_ZONES = [(-480, 0), (960, 1440)]
SPRITE_SCALE = 3
