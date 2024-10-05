from Tile import Tile
from settings import *


class Player(Tile):

    def __init__(self, display, grid_pos, color):
        super().__init__(display, grid_pos, color, collidable=True)
        self.gravity = 2
        self.speed = 10
        self.vel = pygame.math.Vector2(0, 0)
        self.grounded = True
        self.controlling_player = True
        self.grid_pos = pygame.math.Vector2(grid_pos[0], grid_pos[1])
        self.direction = 1
        self.creature = None
        self.can_jump = True
        self.offset = pygame.math.Vector2(0, 600)

    def draw(self, offset):
        pygame.draw.rect(self.display, self.color,
                         (round(self.pos.x - offset.x), round(self.pos.y - offset.y), SCALE, SCALE))
        if self.creature:
            pygame.draw.rect(self.display, self.creature.color,
                             (round(self.creature.pos.x - offset.x), round(self.creature.pos.y - offset.y),
                              self.creature.rect.width, self.creature.rect.height))

    def update(self, keys, tiles, time_passed=0):
        self.update_pos(keys, tiles)
        print(self.controlling_player)
        if self.creature:
            self.creature.update_timer(time_passed)
            if self.creature.destroy_creature:
                self.controlling_player = True
                self.creature = None

    def update_pos(self, keys, tiles):
        moving_person = self if self.controlling_player else self.creature

        self.hit_box.x = self.pos.x
        self.hit_box.y = self.pos.y
        self.vel.y += self.gravity

        if self.creature:
            self.creature.hit_box.x = self.creature.pos.x
            self.creature.hit_box.y = self.creature.pos.y
            self.creature.vel.y += self.creature.gravity

        self.controls(self.creature if not self.controlling_player and self.creature else self, keys)

        self.collide(tiles)
        if self.creature:
            self.creature.collide(tiles)

    def controls(self, moving_person, keys):
        if keys[pygame.K_w] and moving_person.grounded and moving_person.can_jump:
            moving_person.vel.y = -25
            moving_person.grounded = False
        if keys[pygame.K_a]:
            moving_person.set_dir(-moving_person.speed, moving_person.vel.y)
            moving_person.direction = -1
        elif keys[pygame.K_d]:
            moving_person.set_dir(moving_person.speed, moving_person.vel.y)
            moving_person.direction = 1
        else:
            moving_person.set_dir(0, moving_person.vel.y)


    def set_dir(self, dir_x, dir_y):
        self.vel.update(dir_x, dir_y)

    def collide(self, tiles):
        if self.vel.magnitude() == 0:
            return
        future_rect = pygame.Rect(self.hit_box.x + self.vel.x,
                                  self.hit_box.y + self.vel.y,
                                  self.hit_box.width,
                                  self.hit_box.height)

        move = [True, True]
        for tile in tiles:
            if future_rect.colliderect(tile.hit_box):
                if tile.collidable:
                    future_rect_x = pygame.Rect(self.hit_box.x + self.vel.x,
                                                self.hit_box.y,
                                                self.hit_box.width,
                                                self.hit_box.height)
                    future_rect_y = pygame.Rect(self.hit_box.x,
                                                self.hit_box.y + self.vel.y,
                                                self.hit_box.width,
                                                self.hit_box.height)

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
                if tiles_around[i + 1] in [0, 2] and tiles_around[i + 2] in [0, 2]:
                    return int(self.grid_pos.x + self.direction), int(self.grid_pos.y + grid_indexes[i + 1])
        return None

    def summon(self, summon_tile):
        self.creature = CreatureA(self.display, (summon_tile[0], summon_tile[1] - 1), (255, 0, 255))
        self.creature.offset = self.offset.copy()


class Creature(Player):
    def __init__(self, display, grid_pos, color):
        super().__init__(display, grid_pos, color)

        self.disappear_timer = 0
        self.destroy_creature_timer = 5000
        self.destroy_creature = False

    def update_timer(self, time_passed=0):
        self.destroy_creature_timer -= time_passed
        print(time_passed)

        if self.destroy_creature_timer < 0:
            self.destroy_creature = True


class CreatureA(Creature):
    def __init__(self, display, grid_pos, color):
        super().__init__(display, grid_pos, color)
        self.can_jump = False
        self.hit_box = pygame.Rect(self.pos.x, self.pos.y, SCALE, 2 * SCALE)
        self.rect = pygame.Rect(self.pos.x, self.pos.y, SCALE, 2 * SCALE)



class CreatureB(Creature):
    def __init__(self, display, grid_pos, color):
        super().__init__(display, grid_pos, color)


class CreatureC(Creature):
    def __init__(self, display, grid_pos, color):
        super().__init__(display, grid_pos, color)
