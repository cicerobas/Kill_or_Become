from datetime import datetime

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Constants import WIN_WIDTH, WIN_HEIGHT, C_BLOOD_RED, C_WHITE
from code.ScoreDatabaseProxy import ScoreDatabaseProxy


class Score:
    def __init__(self, window: Surface):
        self.window = window
        bg = pygame.image.load("./assets/MenuBG.png")
        self.surf = pygame.transform.scale(bg, (WIN_WIDTH, WIN_HEIGHT))
        self.rect = self.surf.get_rect()
        self.db_name = 'ScoresDatabase'

    def game_over(self, score: int):
        db_proxy = ScoreDatabaseProxy(self.db_name)
        player_name = ""
        running = True
        while running:
            self.window.blit(self.surf, self.rect)
            self.score_text(80, "GAME OVER", C_BLOOD_RED, 100)
            self.score_text(30, f"SCORE: {score}", C_WHITE, 170)
            self.score_text(30, f"ENTER YOUR NAME (4 DIGITS):", C_WHITE, 200)
            self.score_text(30, player_name, C_WHITE, 230)

            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and len(player_name) == 4:
                        db_proxy.save({'name': player_name.upper(), 'score': score, 'date': get_formatted_date()})
                        db_proxy.close()
                        self.show_scores(True)
                        running = False
                    elif event.key == pygame.K_BACKSPACE:
                        player_name = player_name[:-1]
                    else:
                        if len(player_name) < 4:
                            player_name += event.unicode

    def show_scores(self, game_over:bool):
        running = True
        db_proxy = ScoreDatabaseProxy(self.db_name)
        scores = db_proxy.retrieve_top_scores()
        db_proxy.close()

        self.window.blit(self.surf, self.rect)
        self.score_text(50, f"TOP 10 SCORES", C_WHITE, 100)
        self.score_text(30, f"NAME  |  SCORE  |  DATE", C_WHITE, 150)

        for index, score in enumerate(scores):
            id_, name, score, date = score
            self.score_text(30, f'{name}     {score:05d}     {date}', C_WHITE, 180 + 30 * index)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE and not game_over:
                        running = False
                    else:
                        pygame.quit()
                        quit()

            pygame.display.flip()

    def score_text(self, text_size: int, text: str, text_color: tuple, text_y_pos: int):
        text_font: Font = pygame.font.Font("./assets/fonts/Jersey10-Regular.ttf", text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(topleft=(335, text_y_pos))
        self.window.blit(source=text_surf, dest=text_rect)


def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_time} - {current_date}"
