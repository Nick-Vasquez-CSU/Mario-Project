import pygame
from support import import_folder

class Mario(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.animation_import()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations['run_small'][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)

        # Player Movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 7
        self.gravity = 0.8
        self.jump_speed = -22

        # Player Status
        self.status = 'idle_small'
        self.look_right = True
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False
        # 0 = Small Mario, 1 = Big Mario, 2 = Fire Mario
        self.curForm = 0

        # Sound Effects


    def animation_import(self):
        animation_path = f'spritesheets/'
        self.animations = {'idle_small': [], 'run_small': [], 'jump_small': [], 'dead': [], 'grow_small-big': [], 'grow_small-fire': [],
                           'idle_big': [],   'run_big': [],   'jump_big': [],   'duck_big': [],   'grow_big-fire': [],  'shrink_big-small': [],
                           'idle_fire': [],  'run_fire': [],  'jump_fire': [],  'duck_fire': [],  'shrink_fire-small': []}
        # Potential Other Animations: Star Animation
        for animation in self.animations.keys():
            full_path = animation_path + animation
            self.animations[animation] = import_folder(full_path)
        print(self.animations)

    def animate(self):
        animation = self.animations[self.status]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        image = animation[int(self.frame_index)]
        if self.look_right:
            self.image = image
        else:
            flip = pygame.transform.flip(image, True, False)
            self.image = flip

        if self.on_ground and self.on_right:
            self.rect = self.image.get_rect(bottomright=self.rect.bottomright)
        elif self.on_ground and self.on_left:
            self.rect = self.image.get_rect(bottomleft=self.rect.bottomleft)
        elif self.on_ground:
            self.rect = self.image.get_rect(midbottom=self.rect.midbottom)
        elif self.on_ceiling and self.on_right:
            self.rect = self.image.get_rect(topright=self.rect.topright)
        elif self.on_ceiling and self.on_left:
            self.rect = self.image.get_rect(topleft=self.rect.topleft)
        elif self.on_ceiling:
            self.rect = self.image.get_rect(midtop=self.rect.midtop)



    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.look_right = True
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.look_right = False
        elif keys[pygame.K_DOWN] and self.curForm == 1 or 2:
            self.direction.x = 0

        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE] and self.on_ground:
            self.jump()
        if keys[pygame.K_a] and self.curForm == 2:
            pass  # Shoot Fireball

    def get_status(self):
        keys = pygame.key.get_pressed()
        if self.direction.y < 0:
            if self.curForm == 0:
                self.status = 'jump_small'
            elif self.curForm == 1:
                self.status = 'jump_big'
            elif self.curForm == 2:
                self.status = 'jump_fire'
        elif self.direction.y > 1:
            pass
        else:
            if self.direction.x != 0:
                if self.curForm == 0:
                    self.status = 'run_small'
                elif self.curForm == 1:
                    self.status = 'run_big'
                elif self.curForm == 2:
                    self.status = 'run_fire'
            elif keys[pygame.K_DOWN] and self.curForm == 1:
                self.status = 'duck_big'
            elif keys[pygame.K_DOWN] and self.curForm == 2:
                self.status = 'duck_fire'
            else:
                if self.curForm == 0:
                    self.status = 'idle_small'
                elif self.curForm == 1:
                    self.status = 'idle_big'
                elif self.curForm == 2:
                    self.status = 'idle_fire'

    def falling(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        se_jump = pygame.mixer.Sound(f'sounds/Mario_Jump.mp3')
        pygame.mixer.Sound.play(se_jump)
        self.direction.y = self.jump_speed

    def update(self):
        self.get_input()
        self.get_status()
        self.animate()
