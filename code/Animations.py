import pygame
from pygame import Surface

from code.Constants import PLAYER_FRAME_DATA, SPRITE_SCALE, ZOMBIES_FRAME_DATA


def split_sprites(sprite_sheet: Surface, frame_data: tuple) -> list[Surface]:
    frames: list[Surface] = []
    for i in range(frame_data[2]):
        frame = sprite_sheet.subsurface((i * frame_data[0], 0, frame_data[0], frame_data[1]))
        scaled_frame = pygame.transform.scale(frame, (frame_data[0] * SPRITE_SCALE, frame_data[1] * SPRITE_SCALE))
        frames.append(scaled_frame)

    return frames


class Animations:
    def __init__(self, entity_name: str):
        self.entity_name = entity_name
        self.animations: dict[str, tuple] = PLAYER_FRAME_DATA if self.entity_name == "Player" else ZOMBIES_FRAME_DATA[
            entity_name]
        self.animation_frames: dict[str, list[Surface]] = {}
        self.load_animations()

    def load_animations(self):
        for animation in self.animations:
            sprite_sheet = pygame.image.load(f"./assets/sprites/{self.entity_name}/{animation}.png").convert_alpha()
            split_frames = split_sprites(sprite_sheet, self.animations[animation])
            self.animation_frames.update({animation: split_frames})

    def get_frames(self, name: str, flip: bool) -> list[Surface]:
        return [pygame.transform.flip(frame, flip, False) for frame in self.animation_frames.get(name)]
