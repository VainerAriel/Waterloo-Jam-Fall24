from settings import *
from Tile import Tile


class Player(Tile):
    def __init__(self, display, grid_pos, color):
        super().__init__(display, grid_pos, color, collidable=True)
        self.speed = 0.5
        self.vel = pygame.math.Vector2(0, 0)

    def update_pos(self, keys, tiles):
        self.hit_box = pygame.Rect(self.pos.x, self.pos.y, SCALE, SCALE)

        if keys[pygame.K_w]:
            self.set_dir(self.vel.x, -self.speed)
        elif keys[pygame.K_s]:
            self.set_dir(self.vel.x, self.speed)
        else:
            self.set_dir(self.vel.x, 0)

        if keys[pygame.K_a]:
            self.set_dir(-self.speed, self.vel.y)
        elif keys[pygame.K_d]:
            self.set_dir(self.speed, self.vel.y)
        else:
            self.set_dir(0, self.vel.y)

        self.collide(tiles)

    def set_dir(self, dir_x, dir_y):
        self.vel.update(dir_x, dir_y)

    def collide(self, tiles):
        if self.vel.magnitude() == 0:
            return
        future_rect = pygame.Rect(self.pos.x + self.vel.x,
                                  self.pos.y + self.vel.y,
                                  SCALE, SCALE)

        move = [True, True]
        for tile in tiles:
            if future_rect.colliderect(tile.hit_box):
                if tile.collidable:
                    future_rect_x = pygame.Rect(self.pos.x + self.vel.x,
                                                self.pos.y,
                                                SCALE, SCALE)
                    future_rect_y = pygame.Rect(self.pos.x,
                                                self.pos.y + self.vel.y,
                                                SCALE, SCALE)

                    if future_rect_x.colliderect(tile.hit_box):
                        while future_rect_x.colliderect(tile.hit_box):
                            future_rect_x.x -= 1 if self.pos.x < tile.hit_box.x else -1
                        self.pos.x = future_rect_x.x
                        move[0] = False

                    if future_rect_y.colliderect(tile.hit_box):
                        while future_rect_y.colliderect(tile.hit_box):
                            future_rect_y.y -= 1 if self.pos.y < tile.hit_box.y else -1
                        self.pos.y = future_rect_y.y
                        move[1] = False
        if move[0]:
            self.pos.x += self.vel.x
        if move[1]:
            self.pos.y += self.vel.y


class Creature(Player):
    def __init__(self, display, grid_pos, color):
        super().__init__(display, grid_pos, color)


class CreatureA(Creature):
    def __init__(self, display, grid_pos, color):
        super().__init__(display, grid_pos, color)


class CreatureB(Creature):
    def __init__(self, display, grid_pos, color):
        super().__init__(display, grid_pos, color)


class CreatureC(Creature):
    def __init__(self, display, grid_pos, color):
        super().__init__(display, grid_pos, color)
