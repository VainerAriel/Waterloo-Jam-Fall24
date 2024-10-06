from Tile import Tile
from settings import *
from Animation import Animation


class Player(Tile):

    def __init__(self, display, grid_pos, color, images=None):
        super().__init__(display, grid_pos, color, collidable=True, images=None)
        self.gravity = 2.8
        self.speed = 8
        self.vel = pygame.math.Vector2(0, 0)
        self.grounded = True
        self.controlling_player = True
        self.grid_pos = pygame.math.Vector2(grid_pos[0], grid_pos[1])
        self.direction = 1
        self.creature = None
        self.can_jump = True
        self.offset = pygame.math.Vector2(0, 600)
        self.images = idle_anim[0]
        self.summoning = False

        self.idle_a = Animation(8, idle_anim, 0)
        self.walk_a = Animation(8, walk_anim, 0)
        self.jump_a = Animation(8, jump_anim, 1)
        self.summon_a = Animation(8, summon_anim, 1)
        self.summon_p = Animation(8, summon_part, 1)

    def draw(self, offset):
        # if self.summon_a.run_anim:
        #     self.jump_a.draw(self.display, (round(self.rect.x - offset.x), round(self.rect.y - offset.y)),
        #                      self.direction)
        #     if not self.creature == None:
        #         self.summon_p.draw(self.display, (round(self.creature.rect.x - offset.x), round(self.creature.rect.y - offset.y)),
        #                      self.direction)

        # elif self.jump_a.run_anim:
        #     self.jump_a.draw(self.display, (round(self.rect.x - offset.x), round(self.rect.y - offset.y)),
        #                      self.direction)
        # elif self.summon_a.run_anim:
        #     self.summon_a.draw(self.display, (round(self.rect.x - offset.x), round(self.rect.y - offset.y)),
        #                        self.direction)
        # elif self.vel.x == 0 and self.grounded:
        #     self.idle_a.draw(self.display, (round(self.rect.x - offset.x), round(self.rect.y - offset.y)),
        #                      self.direction)
        # else:
        #     self.walk_a.draw(self.display, (round(self.rect.x - offset.x), round(self.rect.y - offset.y)),
                            #  self.direction)

        if self.current_frame >=31: self.current_frame = 0
        if self.images is not None:
        
            if self.direction == 1:
                if self.summoning:
                    self.images = summon_anim[0]
                    if self.anim_frame >= len(self.images):
                        self.anim_frame = 0
                        self.summoning = False
                        self.controlling_player = not self.controlling_player
                    image(self.display, self.images[self.anim_frame], (round(self.rect.x - offset.x), round(self.rect.y - offset.y)))
                    if not self.creature == None:
                        self.images = summon_part[0]
                        
                        image(self.display, self.images[self.anim_frame-2], 
                              (round(self.creature.rect.x - offset.x), 
                               round(self.creature.rect.y - offset.y + SCALE)))
                    if self.current_frame %4 == 0: self.anim_frame +=1

                elif self.vel.x == 0 and self.grounded:
                    self.images = idle_anim[0]
                    if self.anim_frame >= len(self.images): self.anim_frame = 0
                    image(self.display, self.images[self.anim_frame], (round(self.rect.x - offset.x), round(self.rect.y - offset.y)))
                    if self.current_frame %4 == 0: self.anim_frame+=1
                else:
                    self.images = walk_anim[0]
                    if self.anim_frame >= len(self.images): self.anim_frame = 0
                    image(self.display, self.images[self.anim_frame], (round(self.rect.x - offset.x), round(self.rect.y - offset.y)))
                    if self.current_frame %4 == 0:self.anim_frame+=1
        
            else:
                if self.summoning:
                    self.images = summon_anim[1]
                    if self.anim_frame >= len(self.images):
                        self.anim_frame = 0
                        self.summoning = False
                        self.controlling_player = not self.controlling_player
                    image(self.display, self.images[self.anim_frame], (round(self.rect.x - offset.x), round(self.rect.y - offset.y)))
                    if not self.creature == None:
                        self.images = summon_part[1]
                        
                        image(self.display, self.images[self.anim_frame-2], 
                              (round(self.creature.rect.x - offset.x), 
                               round(self.creature.rect.y - offset.y + SCALE)))
                    if self.current_frame %4 == 0: self.anim_frame +=1

                elif self.vel.x == 0 and self.grounded:
                    self.images = idle_anim[1]
                    if self.anim_frame >= len(self.images): self.anim_frame = 0
                    image(self.display, self.images[self.anim_frame], (round(self.rect.x - offset.x), round(self.rect.y - offset.y)))
                    if self.current_frame %4 == 0:self.anim_frame+=1
        
                else:
                    self.images = walk_anim[1]
                    if self.anim_frame >= len(self.images): self.anim_frame = 0
                    image(self.display, self.images[self.anim_frame], (round(self.rect.x - offset.x), round(self.rect.y - offset.y)))
                    if self.current_frame %4 == 0:self.anim_frame+=1
        if False:
            print("Bbbbbbbbbbbbbbbbbbbbbbbbbb")
            pygame.draw.rect(self.display, self.color,
                            (round(self.rect.x - offset.x), round(self.rect.y - offset.y), SCALE, SCALE))
        # if self.creature:
        #     pygame.draw.rect(self.display, self.creature.color,
        #                      (round(self.creature.rect.x - offset.x), round(self.creature.rect.y - offset.y),
        #                       self.creature.rect.width, self.creature.rect.height))

        self.current_frame += 1

    def update(self, keys, tiles, time_passed=0):
        self.update_pos(keys, tiles)
        if self.creature:
            self.creature.update_timer(time_passed)
            if self.creature.destroy_creature:
                self.controlling_player = True
                self.creature = None
                for tile in tiles:
                    if tile.picked_up:
                        tile.picked_up = False
                        tile.drop = True

        self.idle_a.update()
        self.walk_a.update()
        self.jump_a.update(1 if self.vel.y > 0 else 2)
        self.summon_a.update()

    def update_pos(self, keys, tiles):
        self.hit_box.x = self.rect.x
        self.hit_box.y = self.rect.y
        self.vel.y += self.gravity

        if self.creature:
            self.creature.hit_box.x = self.creature.rect.x
            self.creature.hit_box.y = self.creature.rect.y
            self.creature.vel.y += self.creature.gravity

        self.controls(self.creature if not self.controlling_player and self.creature else self, keys)

        self.collide(tiles)
        if self.creature:
            self.creature.collide(tiles)

    def controls(self, moving_person, keys):
        if not self.summoning:
            if keys[pygame.K_w] and moving_person.grounded and moving_person.can_jump:
                moving_person.vel.y = -22
                moving_person.grounded = False
                self.jump_a.start()
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
            if future_rect.colliderect(tile.rect):
                if tile.collidable:
                    future_rect_x = pygame.Rect(self.hit_box.x + self.vel.x,
                                                self.hit_box.y,
                                                self.hit_box.width,
                                                self.hit_box.height)
                    future_rect_y = pygame.Rect(self.hit_box.x,
                                                self.hit_box.y + self.vel.y,
                                                self.hit_box.width,
                                                self.hit_box.height)

                    if future_rect_x.colliderect(tile.rect):
                        while future_rect_x.colliderect(tile.rect):
                            future_rect_x.x -= 1 if self.rect.x < tile.rect.x else -1
                        self.rect.x = future_rect_x.x
                        move[0] = False
                    if future_rect_y.colliderect(tile.rect):
                        while future_rect_y.colliderect(tile.rect):
                            future_rect_y.y -= 1 if self.rect.y < tile.rect.y else -1

                        if self.rect.y <= tile.rect.y:
                            self.grounded = True
                            self.jump_a.reset()
                        self.rect.y = future_rect_y.y
                        self.vel.y = 0

                        move[1] = False
        if move[0]:
            self.rect.x += self.vel.x
        if move[1]:
            self.rect.y += self.vel.y

        if self.vel.y != 0:
            self.grounded = False

    def update_grid_loc(self, level, movable_tiles):
        self.grid_pos.update(round(self.rect.x / SCALE), round(self.rect.y / SCALE))
        for y in range(len(level)):
            for x in range(len(level[y])):
                if level[y][x] == 3:
                    level[y][x] = 0

        for tile in movable_tiles:
            tile_grid_x = tile.rect.x / SCALE
            tile_grid_y = round(tile.rect.y / SCALE)

            level[tile_grid_y][int(tile_grid_x // 1)] = 3
            if tile_grid_x != round(tile_grid_x):
                level[tile_grid_y][int(tile_grid_x // 1) + 1] = 3
        return level

    def convert_to_dict(self, movable_tiles):
        moveable = {}
        for tile in movable_tiles:
            tile_grid_x = round(tile.rect.x / SCALE)
            tile_grid_y = round(tile.rect.y / SCALE)
            moveable[(tile_grid_x, tile_grid_y)] = tile
        return moveable

    def check_tile_nearby(self, level, movable_tiles):
        level_updated = self.update_grid_loc(level, movable_tiles)
        tiles_around = []
        grid_indexes = []
        if self.grid_pos.y + 2 < grid_h:
            tiles_around.append(level_updated[int(self.grid_pos.y + 2)][int(self.grid_pos.x + self.direction)])
            grid_indexes.append(2)
        for i in range(1, -4, -1):
            tiles_around.append(level_updated[int(self.grid_pos.y + i)][int(self.grid_pos.x + self.direction)])
            grid_indexes.append(i)
        for i, tile_type in enumerate(tiles_around):
            if tile_type in [1, 3] and i < (3 if self.grid_pos.y + 2 < grid_h else 2):
                if tiles_around[i + 1] in [0, 2] and tiles_around[i + 2] in [0, 2]:
                    return int(self.grid_pos.x + self.direction), int(self.grid_pos.y + grid_indexes[i + 1])
        return None

    def summon(self, summon_tile):
        self.creature = CreatureA(self.display, (summon_tile[0], summon_tile[1] - 1), (255, 0, 255))
        self.creature.offset = self.offset.copy()


class Creature(Player):
    def __init__(self, display, grid_pos, color):
        super().__init__(display, grid_pos, color, images=None)

        self.disappear_timer = 0
        self.destroy_creature_timer = 15000
        self.destroy_creature = False

    def update_timer(self, time_passed=0):
        self.destroy_creature_timer -= time_passed

        if self.destroy_creature_timer < 0:
            self.destroy_creature = True


class CreatureA(Creature):
    def __init__(self, display, grid_pos, color):
        super().__init__(display, grid_pos, color)
        self.can_jump = False
        self.hit_box = pygame.Rect(self.rect.x, self.rect.y, SCALE, 2 * SCALE)
        self.grab_box = pygame.Rect(self.rect.x + (SCALE if self.direction == 1 else -SCALE / 2),
                                    self.rect.y + SCALE, SCALE / 2, SCALE)
        self.rect = pygame.Rect(self.rect.x, self.rect.y, SCALE, 2 * SCALE)
        self.can_pickup = False

        self.stack = []

    def check_pickup(self, tile):
        return tile.movable and self.grab_box.colliderect(tile.rect) and not tile.drop

    def pickup(self, tiles, movable_tiles, level, player):
        movable = self.convert_to_dict(movable_tiles)

        self.grab_box = pygame.Rect(self.rect.x + (SCALE if self.direction == 1 else -SCALE / 2),
                                    self.rect.y + SCALE, SCALE / 2, SCALE)

        for tile in tiles:
            if self.check_pickup(tile):
                location = round(tile.rect.x / SCALE), round(tile.rect.y / SCALE)
                self.stack = []
                i = 0
                while (location[0], location[1] - i) in movable.keys():
                    self.stack.append(movable[(location[0], location[1] - i)])
                    i += 1

                loc = round(self.stack[-1].rect.y / SCALE), round(self.stack[-1].rect.x / SCALE)
                if not (level[loc[0] - 1][loc[1]] in [0, 2] and level[loc[0] - 2][loc[1]] in [0, 2]):
                    self.stack = []

                fakerect = pygame.Rect(player.rect.x, player.rect.y + 4, player.rect.width, player.rect.height)
                print(fakerect)
                print(level[round(player.rect.y / SCALE) - 2][round(player.rect.x / SCALE)])
                if fakerect.colliderect(self.stack[-1].rect) and (
                        level[round(player.rect.y / SCALE) - 2][round(player.rect.x / SCALE)] in [0, 2]):
                    player.rect.y -= SCALE * 2
                elif not (level[round(player.rect.y / SCALE) - 2][round(player.rect.x / SCALE)] in [0, 2]):
                    self.stack = []
                # if not level[location[1] - i - 1][location[0]] in [0, 2]:
                #     self.stack = []
                #     break

                print(self.stack)
                for i, box in enumerate(self.stack):
                    box.rect.y -= 2 * SCALE
                    self.rect.x = box.rect.x
                    box.picked_up = True
                    box.id = i
                    print(box.id)


class CreatureB(Creature):
    def __init__(self, display, grid_pos, color):
        super().__init__(display, grid_pos, color)


class CreatureC(Creature):
    def __init__(self, display, grid_pos, color):
        super().__init__(display, grid_pos, color)
