import pygame


class UI:
    def __init__(self, surface):
        self.display_surface = surface
        self.font = pygame.font.SysFont(None, 50)

    def show_score(self, amount):
        score_amount_surface = self.font.render('Score: ' + str(amount), False, '#33323d')
        score_amount_rect = score_amount_surface.get_rect(midleft=(0, 100))
        self.display_surface.blit(score_amount_surface, score_amount_rect)

    def show_coins(self, amount):
        coin_amount_surface = self.font.render('Coins: ' + str(amount), False, '#33323d')
        coin_amount_rect = coin_amount_surface.get_rect(midleft = (300, 100))
        self.display_surface.blit(coin_amount_surface, coin_amount_rect)

    def show_level(self, level):
        level_surface = self.font.render('Level: ' + level, False, '#33323d')
        level_rect = level_surface.get_rect(midleft=(600, 100))
        self.display_surface.blit(level_surface, level_rect)

    def show_time(self, time):
        time_surface = self.font.render('Time: ' + str(time), False, '#33323d')
        time_rect = time_surface.get_rect(midleft=(900, 100))
        self.display_surface.blit(time_surface, time_rect)
