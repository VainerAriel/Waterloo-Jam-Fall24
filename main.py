import sys

from settings import *


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 255))
        pygame.display.update()

def main_menu():
    btn = pygame.Rect(500 * RESIZE, 700 * RESIZE, 300 * RESIZE, 100 * RESIZE)

    state = "main menu"

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        mx, my = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()[0]

        if state == "game":
            main()
        else:
            screen.fill((255, 0, 0))
            pygame.draw.rect(screen, (255, 255, 255), btn)

        if pygame.Rect(500*RESIZE, btn.y, btn.width, btn.height).collidepoint(mx, my):
            btn.x = btn.x + (550*RESIZE - btn.x) * 0.1
            if click:
                state = "game"
        else:
            btn.x = btn.x + (500*RESIZE - btn.x) * 0.1

        clock.tick(FPS)
        pygame.display.update()


main_menu()