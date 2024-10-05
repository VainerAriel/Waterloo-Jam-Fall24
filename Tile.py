from settings import *


# class for defining tiles
class Tile:
    def __init__(self, display, grid_pos, color, collidable=False):
        self.display = display
        self.pos = pygame.math.Vector2(grid_pos[0] * SCALE, grid_pos[1] * SCALE)
        self.color = color
        self.hit_box = pygame.Rect(self.pos.x, self.pos.y, SCALE, SCALE)
        self.collidable = collidable

    # function for drawing tiles
    def draw(self, offset):
        pygame.draw.rect(self.display, self.color,
                         (round(self.pos.x - offset.x), round(self.pos.y - offset.y), SCALE, SCALE))
