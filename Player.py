from settings import *
from Tile import Tile


class Player(Tile):
    def __init__(self, display, grid_pos, color):
        super().__init__(display, grid_pos, color)
        self.speed = 2

    def update_pos(self, keys):
        if keys[pygame.K_w]:
            self.pos.y -= self.speed*RESIZE
        if keys[pygame.K_d]:
            self.pos.x += self.speed*RESIZE
        if keys[pygame.K_s]:
            self.pos.y += self.speed*RESIZE
        if keys[pygame.K_a]:
            self.pos.x -= self.speed*RESIZE


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
