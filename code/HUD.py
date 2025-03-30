import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Constants import WIN_HEIGHT, C_WHITE, PLAYER_MAX_HEALTH, C_DARK_GREY, C_GREEN


class HUD:
    def __init__(self, window: Surface):
        self.window = window
        self.ammo_icon = pygame.transform.scale(pygame.image.load("./assets/sprites/Hud/ammo.png").convert_alpha(),
                                                (40, 40))
        self.ammo_icon_rect = self.ammo_icon.get_rect(topleft=(10, (WIN_HEIGHT - 40)))

    def draw(self, player_hp, gun_ammo, total_ammo, score):
        hp_ratio = player_hp / PLAYER_MAX_HEALTH
        pygame.draw.rect(self.window, C_DARK_GREY, pygame.Rect(10, 10, 200, 20), 2)
        pygame.draw.rect(self.window, C_GREEN, pygame.Rect(10, 10, 200 * hp_ratio, 20), )

        self.hud_text(f"SCORE: {score}", (10, (WIN_HEIGHT - 70)))
        self.window.blit(self.ammo_icon, self.ammo_icon_rect)
        self.hud_text(f"{gun_ammo}/{total_ammo}",
                      (self.ammo_icon.get_width() + 10, (WIN_HEIGHT - 40)))

    def hud_text(self, text: str, text_pos: tuple):
        text_font: Font = pygame.font.Font("./assets/fonts/Jersey10-Regular.ttf", 30)
        text_surf: Surface = text_font.render(text, True, C_WHITE).convert_alpha()
        text_rect: Rect = text_surf.get_rect(topleft=text_pos)
        self.window.blit(text_surf, text_rect)
