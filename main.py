from settings import *

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    screen.fill((255, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), (0, 0, 960*RESIZE, 540*RESIZE))
    pygame.display.update()
    