import pygame
from support import import_folder
from tiles import AnimatedTile


class Enemy(AnimatedTile):
    def __init__(self, pos, size, type = None):
        self.type = type
        if self.type == 'G':
            super().__init__(pos, size, type, f'spritesheets/goomba_move')
        elif self.type == 'K':
            super().__init__(pos, size, type, f'spritesheets/koopa_move')
            self.rect.y += size - self.image.get_size()[1]
        self.speed = 5

    def move(self):
        self.rect.x += self.speed

    def reverse_image(self):
        if self.speed > 0:
            self.image = pygame.transform.flip(self.image, True, False)

    def reverse(self):
        self.speed *= -1

    def update(self, shift):
        self.rect.x += shift
        self.animate()
        self.move()
        self.reverse_image()
