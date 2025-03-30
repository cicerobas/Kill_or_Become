import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Constants import WIN_WIDTH, WIN_HEIGHT, C_BLOOD_RED, MENU_OPTIONS, C_WHITE


class Menu:
    def __init__(self, window: Surface):
        self.window = window
        bg = pygame.image.load("./assets/MenuBG.png")
        self.surf = pygame.transform.scale(bg, (WIN_WIDTH, WIN_HEIGHT))
        self.rect = self.surf.get_rect()

    def run(self):
        pygame.mixer_music.load('./assets/sounds/Menu.mp3')
        pygame.mixer_music.set_volume(0.3)
        pygame.mixer_music.play(-1)
        menu_option = 0
        clock = pygame.time.Clock()
        while True:
            clock.tick(30)
            self.window.blit(self.surf, self.rect)
            self.menu_text(80, "Kill or", C_BLOOD_RED, (30, 30))
            self.menu_text(80, "Become", C_BLOOD_RED, (30, 90))

            for i in range(len(MENU_OPTIONS)):
                if i == menu_option:
                    self.menu_text(40, MENU_OPTIONS[i], C_BLOOD_RED, (30, 220 + 40 * i))
                else:
                    self.menu_text(40, MENU_OPTIONS[i], C_WHITE, (30, 220 + 40 * i))

            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTIONS) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTIONS) - 1
                    if event.key == pygame.K_RETURN:
                        if menu_option != 1:
                            pygame.mixer_music.stop()
                        return MENU_OPTIONS[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.Font("./assets/fonts/Jersey10-Regular.ttf", text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(topleft=text_pos)
        self.window.blit(source=text_surf, dest=text_rect)
