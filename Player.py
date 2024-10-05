from settings import *
from Tile import Tile


class Player(Tile):
    def __init__(self, display, grid_pos, color):
        super().__init__(display, grid_pos, color)
        self.speed = 0.5
        velocity = 0
    def update_pos(self, keys):
        if keys[pygame.K_w]:
            velocity = 60
            self.pos.y -= self.velocity
        if keys[pygame.K_d]:
            self.pos.x += self.speed
        if keys[pygame.K_s]:
            self.pos.y += self.speed
        if keys[pygame.K_a]:
            self.pos.x -= self.speed


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
