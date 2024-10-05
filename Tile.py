from settings import *


# class for defining tiles
class Tile:
    def __init__(self, display, grid_pos, color, collidable=False, movable=False):
        self.display = display
        self.color = color
        self.rect = pygame.Rect(grid_pos[0] * SCALE, grid_pos[1] * SCALE, SCALE, SCALE)
        self.hit_box = pygame.Rect(self.rect.x, self.rect.y, SCALE, SCALE)
        self.collidable = collidable
        self.movable = movable
        self.picked_up = False
        self.drop = False
        self.goal = -1
        self.collide_with = None

    # function for drawing tiles
    def draw(self, offset):
        if not self.drop:
            pygame.draw.rect(self.display, self.color,
                             (round(self.rect.x - offset.x), round(self.rect.y - offset.y), self.rect.width,
                              self.rect.height))
        else:
            pygame.draw.rect(self.display, (200, 200, 0),
                             (round(self.rect.x - offset.x), round(self.rect.y - offset.y), self.rect.width,
                              self.rect.height))

    def update_movable_tile(self, tiles, player):
        if self.picked_up:
            if player.creature:
                self.rect.x = player.creature.rect.x
                self.rect.y = player.creature.rect.y-SCALE
        if self.drop:
            if self.goal == -1:
                print("aa")
                collide = False
                fake_tile = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, self.rect.height)

                while not collide:
                    fake_tile.y += SCALE
                    for tile in tiles:
                        if self != tile and tile.collidable:
                            if fake_tile.colliderect(tile):
                                print(tile, self)
                                pygame.draw.rect(screen, (0, 255, 255), tile.rect)
                                self.goal = tile.rect.y - SCALE
                                collide = True
                print(self.goal)
            if self.rect.y < self.goal:
                self.rect.y += 4
                if self.rect.colliderect(player.hit_box):
                    self.rect.y = player.hit_box.y-SCALE
                if player.creature:
                    if self.rect.colliderect(player.creature.hit_box):
                        self.rect.y = player.creature.hit_box.y - SCALE
                print("add")
            else:
                self.rect.y = self.goal

            can_disappear = True
            if self.rect.colliderect(player.hit_box):
                if self.collide_with is None:
                    self.collide_with = 1
                can_disappear = False
            if player.creature:
                if self.rect.colliderect(player.creature.hit_box):
                    if self.collide_with is None:
                        self.collide_with = 2
                    can_disappear = False

            if can_disappear and self.rect.y == self.goal:
                self.collide_with = None
                self.drop = False
                self.goal = -1


