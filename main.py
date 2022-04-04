import pygame
import sys
from settings import *
from level import Level
from ui import UI
from mainmenu import Menu

class Game:
    def __init__(self):
        self.max_level = 1
        self.mainmenu = Menu(0, self.max_level, screen)
        self.lives = 3
        self.points = 0
        self.ui = UI(screen)

    def create_level(self, current_level):
        pass

    def create_mainmenu(self):
        pass

    def run(self):
        self.mainmenu.run()


pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
bg = pygame.image.load(f'spritesheets/level_bg.png')
clock = pygame.time.Clock()
#game = Game()
level = Level(level_map, screen)

pygame.mixer.music.load(f'sounds/Super_Mario_Bros_NES.mp3')
pygame.mixer.music.play(-1)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(bg, [0, -60])
    #screen.fill('black')
    #game.run()
    level.run()

    pygame.display.update()
    clock.tick(60)
