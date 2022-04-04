import pygame

GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (130, 130, 130)


class Menu:
    def __init__(self, game, screen):
        self.screen = screen
        self.landing_page_finished = False
        self.highscore = game.stats.get_highscore()

        headingFont = pygame.font.SysFont(None, 192)
        subheadingFont = pygame.font.SysFont(None, 122)
        font = pygame.font.SysFont(None, 48)

        strings = [(f'HIGH SCORE = {self.highscore:,}', GREY, font)]
        self.texts = [self.get_text(msg=s[0], color=s[1], font=s[2]) for s in strings]
        self.posns = [150, 230]

        centerx = self.screen.get_rect().centerx

        n = len(self.texts)
        self.rects = [self.get_text_rect(text=self.texts[i], centerx=centerx, centery=self.posns[i]) for i in range(n)]

    def get_text(self, font, msg, color): return font.render(msg, True, color, BLACK)

    def get_text_rect(self, text, centerx, centery):
        rect = text.get_rect()
        rect.centerx = centerx
        rect.centery = centery
        return rect

    def show(self):
        while not self.landing_page_finished:
            self.update()
            self.draw()
            self.check_events()   # exits game if QUIT pressed

    def draw_text(self):
        n = len(self.texts)
        for i in range(n):
            self.screen.blit(self.texts[i], self.rects[i])

    def draw(self):
        self.screen.blit()
        self.draw_text()
        pygame.display.flip()
