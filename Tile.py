from settings import *

class Tile:
    def __init__(self, display, grid_pos, color):
        self.display = display
        self.pos = pygame.math.Vector2(grid_pos[0] * SCALE, grid_pos[1] * SCALE)
        self.color = color

    def draw(self, offset):
        pygame.draw.rect(self.display, self.color, (self.pos.x-offset.x, self.pos.y-offset.y, SCALE, SCALE))
