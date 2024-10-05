import pygame

pygame.init()
# size of screen in terms of tiles
grid_w, grid_h = 24, 20

SCALE = 60 # size of tiles in pixels
WIDTH, HEIGHT = 12 * SCALE, 10 * SCALE
screen = pygame.display.set_mode((WIDTH, HEIGHT))

FPS = 30 # sets framrate constant

#sets name of window
pygame.display.set_caption("Waterloo Jam!!")
clock = pygame.time.Clock()

#function for loading in images
def loadify(filename, scaling):
    img = pygame.image.load(filename).convert_alpha()
    img = pygame.transform.scale(img, (img.get_width() * scaling, img.get_height() * scaling))
    return img

#function for displaying images
def image(surface, img, pos, mode="corner"):
    if mode == "center":
        surface.blit(img, (pos[0] - img.get_width() / 2, pos[1] - img.get_height() / 2))
    else:
        surface.blit(img, pos)


comic_sans_font = pygame.font.SysFont("comicsansms", 50)

#function for displaying text
def text(surface, _string, f_n, color, pos, mode):
    f = f_n
    string = f.render(_string, True, color)
    string_rect = string.get_rect()

    if mode == "corner":
        string_rect.topleft = pos
    else:
        string_rect.center = pos

    surface.blit(string, string_rect)

#function for fading levels to mask loading
def fade(surface, mode, draw_func, *draw_par):
    fade_surf = pygame.Surface((WIDTH, HEIGHT))
    fade_surf.fill((0, 0, 0))
    alpha = 255 if mode == "in" else 0
    step = -2.5 if mode == "in" else 2.5
    while (mode == "in" and alpha >= 0) or (mode == "out" and alpha <= 255):
        fade_surf.set_alpha(alpha)
        draw_func(*draw_par)
        surface.blit(fade_surf, (0, 0))
        pygame.display.update()
        alpha += step
        pygame.time.delay(2)
        clock.tick()

