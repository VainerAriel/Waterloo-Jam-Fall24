from settings import *


# class for defining tiles
class Tile:
    def __init__(self, display, grid_pos, color, collidable=False, movable=False, images=None):
        self.display = display
        self.color = color
        self.rect = pygame.Rect(grid_pos[0] * SCALE, grid_pos[1] * SCALE, SCALE, SCALE)
        self.collidable = collidable
        self.movable = movable
        self.picked_up = False
        self.drop = False
        self.goal = -1
        self.id = 0
        self.images = images
        self.anim_frame = 0
        self.current_frame = 0
        self.show_tile = True

    # function for drawing tiles
    def draw(self, offset):
        if self.collidable and self.show_tile:
            image(self.display, box, (round(self.rect.x - offset.x), round(self.rect.y - offset.y), self.rect.width,
                          self.rect.height))
        # pygame.draw.rect(self.display, self.color,
        #                  (round(self.rect.x - offset.x), round(self.rect.y - offset.y), self.rect.width,
        #                   self.rect.height))

    def update_movable_tile(self, tiles, player):
        if self.picked_up:
            if player.creature:
                future_rect = pygame.Rect(player.creature.rect.x-player.creature.rect.width/2 + 5, self.rect.y, self.rect.width, self.rect.height)
                print(future_rect)
                move = True
                for tile in tiles:
                    if future_rect.colliderect(tile.rect) and tile.collidable and self != tile:
                        move = False
                        print(tile.rect)
                        for s in player.creature.stack:
                            s.picked_up = False
                            s.drop = True

                if move:
                    self.rect.x = player.creature.rect.x-player.creature.rect.width/2+5
                # self.rect.y = player.creature.rect.y-SCALE
        if self.drop:
            if self.goal == -1:
                if abs(self.rect.x - (self.rect.x // SCALE * SCALE)) < 15:
                    self.rect.x = (self.rect.x // SCALE * SCALE)
                if abs(self.rect.x - (self.rect.x // SCALE * SCALE + SCALE)) < 15:
                    self.rect.x = (self.rect.x // SCALE * SCALE) + SCALE

                collide = False
                fake_tile = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, self.rect.height)

                while not collide:
                    fake_tile.y += SCALE
                    for tile in tiles:
                        if self != tile and tile.collidable and not tile.movable:
                            if fake_tile.colliderect(tile):
                                # pygame.draw.rect(screen, (0, 255, 255), tile.rect)
                                self.goal = tile.rect.y - SCALE - SCALE * self.id
                                collide = True
            if self.rect.y < self.goal:
                self.rect.y += 12
                if self.rect.colliderect(player.hit_box):
                    self.rect.y = player.hit_box.y-SCALE
                if player.creature:
                    if self.rect.colliderect(player.creature.hit_box):
                        self.rect.y = player.creature.hit_box.y - SCALE
                for tile in tiles:
                    if self != tile and tile.collidable:
                        if self.rect.colliderect(tile):
                            self.rect.y = tile.rect.y - SCALE
            else:
                self.rect.y = self.goal - SCALE * self.id

            can_disappear = True
            if self.rect.colliderect(player.hit_box):
                can_disappear = False
            if player.creature:
                if self.rect.colliderect(player.creature.hit_box):
                    can_disappear = False

            if can_disappear and self.rect.y == self.goal:
                self.drop = False
                self.goal = -1
                self.id = 0
                player.stack = []



