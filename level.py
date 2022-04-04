import pygame
from tiles import Tile, BreakableBrick
from settings import tile_size, screen_width, screen_height
from player import Mario
from enemy import Enemy
from ui import UI

#screen = pygame.display.set_mode((screen_width, screen_height))
#bg = pygame.image.load(f'spritesheets/level_bg.png')



class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0
        self.screen_x = 0
        self.ui = UI(self.display_surface)
        self.timer = 300
        self.score = 0

    def setup_level(self, layout):

        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.goal = pygame.sprite.GroupSingle()
        self.foes = pygame.sprite.Group()
        self.constraints = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size

                if cell == 'X':  # Ground_Brick
                    tile = Tile((x, y), tile_size, 0)
                    self.tiles.add(tile)
                if cell == 'R':  # Stair_Brick
                    tile = Tile((x, y), tile_size, 1)
                    self.tiles.add(tile)
                if cell == 'N':  # Blue_Stone
                    tile = Tile((x, y), tile_size, 2)
                    self.tiles.add(tile)
                if cell == 'A':  # Blue_Brick
                    tile = Tile((x, y), tile_size, 3)
                    self.tiles.add(tile)
                if cell == 'C':  # Coin
                    tile = Tile((x, y), tile_size, 4)
                    self.tiles.add(tile)
                if cell == 'G':  # Goomba
                    enemy = Enemy((x, y), tile_size, 'G')
                    self.foes.add(enemy)
                if cell == 'K':  # Koopa
                    enemy = Enemy((x, y), tile_size, 'K')
                    self.foes.add(enemy)
                if cell == 'P':  # Player
                    player_sprite = Mario((x, y))
                    self.player.add(player_sprite)
                if cell == 'F':  # Flag
                    goal_sprite = Tile((x, y), tile_size, 5)
                    self.goal.add(goal_sprite)
                if cell == 'Z':  # Enemy Constraints
                    constraint = Tile((x, y), tile_size)
                    self.constraints.add(constraint)
                if cell == 'B':  # Breakable Brick
                    brick = BreakableBrick((x, y), tile_size)
                    self.tiles.add(brick)
                if cell == 'M' or cell == '?':
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)

        print(self.tiles.sprites())

    def enemy_collision_reverse(self):
        for enemy in self.foes.sprites():
            if pygame.sprite.spritecollide(enemy, self.constraints, False):
                enemy.reverse()

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        # Camera Logic
        if player_x < 30 and direction_x < 0:
            player.speed = 0
        elif player_x > screen_width / 2 and direction_x > 0:
            self.world_shift = -7
            player.speed = 0
            #screen.blit(bg, [self.screen_x, -60])
            #self.screen_x -= 1
        else:
            self.world_shift = 0
            player.speed = 7

    def horizontal_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def verticle_collision(self):
        player = self.player.sprite
        player.falling()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True
                    if isinstance(sprite, BreakableBrick) and self.player.sprite.curForm >= 1:
                        se_break = pygame.mixer.Sound(f'sounds/Mario_Break.mp3')
                        pygame.mixer.Sound.play(se_break)
                        self.score += 100
                        sprite.kill()

        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False
        if player.on_ceiling and player.direction.y > 0:
            player.on_ceiling = False

    def run(self):

        # Main Blocks
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.scroll_x()

        # Player
        self.player.update()
        self.horizontal_collision()
        self.verticle_collision()
        self.player.draw(self.display_surface)

        self.goal.update(self.world_shift)
        self.goal.draw(self.display_surface)

        # Enemies
        self.foes.update(self.world_shift)
        self.constraints.update(self.world_shift)
        self.enemy_collision_reverse()
        self.foes.draw(self.display_surface)

        # Show Score
        self.ui.show_score(self.score)
        self.ui.show_coins(0)
        self.ui.show_level('1-1')
        self.ui.show_time(self.timer)



