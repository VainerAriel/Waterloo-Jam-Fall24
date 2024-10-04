import pygame
pygame.init()


WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode((WIDTH, HEIGHT))

RESIZE = WIDTH/1920

RED = (255, 0, 0)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    screen.fill(RED)
    pygame.draw.rect(screen, (255, 255, 255), (0, 0, 960*RESIZE, 540*RESIZE))
    pygame.display.update()
    