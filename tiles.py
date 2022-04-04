import pygame
from support import import_folder


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size, type = None):
        super().__init__()
        self.type = type
        if self.type == 0:
            self.image = pygame.image.load(f'spritesheets/Ground_Brick.png')
        elif self.type == 1:
            self.image = pygame.image.load(f'spritesheets/Stair_Brick.png')
        elif self.type == 2:
            self.image = pygame.image.load(f'spritesheets/Blue_Stone.png')
        elif self.type == 3:
            self.image = pygame.image.load(f'spritesheets/Blue_Brick.png')
        elif self.type == 4:
            self.image = pygame.image.load(f'spritesheets/Coin.png')
        elif self.type == 5:
            self.image = pygame.image.load(f'spritesheets/flag.png')
        else:
            self.image = pygame.Surface((size, size))
            self.image.fill('grey')
        self.rect = self.image.get_rect(topleft=pos)
        self.rect.y += size - self.image.get_size()[1]

    def update(self, x_shift):
        self.rect.x += x_shift

class AnimatedTile(Tile):
    def __init__(self, pos, size, type = None, path = None):
        super().__init__(pos, size)
        self.frames = import_folder(path)
        self.frame_index = 0
        self.image = self.frames[self.frame_index]

    def animate(self):
        self.frame_index += 0.15
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]

    def update(self, shift):
        self.animate()
        self.rect.x += shift


class BreakableBrick(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.image.load(f'spritesheets/brick_float_0.png')
        self.rect = self.image.get_rect(topleft=pos)
        self.rect.y += size - self.image.get_size()[1]
        self.isB = True

    def update(self, x_shift):
        self.rect.x += x_shift

