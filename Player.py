from settings import *
from Tile import Tile


class Player(Tile):
    
    def __init__(self, display, grid_pos, color):
        super().__init__(display, grid_pos, color, collidable=True)
        self.gravity = 2
        self.speed = 10
        self.vel = pygame.math.Vector2(0, 0)
        self.grounded = True
        self.movable = True
        self.grid_pos = pygame.math.Vector2(grid_pos[0], grid_pos[1])
        self.direction = 1

    def update_pos(self, keys, tiles):
        print(self.vel.y)
        self.hit_box = pygame.Rect(self.pos.x, self.pos.y, SCALE, SCALE)
        self.vel.y += self.gravity
        print(self.movable)
        

        if self.movable:
            if keys[pygame.K_w] and self.grounded:
                self.vel.y = -25
                self.grounded = False
            if keys[pygame.K_a]:
                self.set_dir(-self.speed, self.vel.y)
                self.direction = -1
            elif keys[pygame.K_d]:
                self.set_dir(self.speed, self.vel.y)
                self.direction = 1
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
                        
                        if self.pos.y <= tile.hit_box.y:
                            self.grounded = True
                        self.pos.y = future_rect_y.y
                        self.vel.y = 0
                        
                        move[1] = False
        if move[0]:
            self.pos.x += self.vel.x
        if move[1]:
            self.pos.y += self.vel.y

        if self.vel.y != 0:
            self.grounded = False

    def update_grid_loc(self):
        self.grid_pos.update(round(self.pos.x / SCALE), round(self.pos.y / SCALE))
    def check_tile_nearby(self, level):
        self.update_grid_loc()
        print(self.grid_pos)
        tiles_around = []
        grid_indexes = []
        if self.grid_pos.y + 2 < grid_h:
            tiles_around.append(level[int(self.grid_pos.y + 2)][int(self.grid_pos.x + self.direction)])
            grid_indexes.append(2)
        for i in range(1, -4, -1):
            tiles_around.append(level[int(self.grid_pos.y + i)][int(self.grid_pos.x + self.direction)])
            grid_indexes.append(i)
        print(tiles_around)
        for i, tile_type in enumerate(tiles_around):
            if tile_type == 1 and i < (3 if self.grid_pos.y + 2 < grid_h else 2):
                if tiles_around[i+1] in [0, 2] and tiles_around[i+2] in [0, 2]:
                    return int(self.grid_pos.y + grid_indexes[i+1]), int(self.grid_pos.x + self.direction)
        return None




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
