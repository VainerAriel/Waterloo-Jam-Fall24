import sys

import pygame.key

from levels import *


def main():
    level = load_level(BASE_WORLD)
    tiles, player = level

    offset = pygame.math.Vector2(0, 10 * SCALE)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            offset.y -= 1*RESIZE
        if keys[pygame.K_d]:
            offset.x += 1*RESIZE
        if keys[pygame.K_s]:
            offset.y += 1*RESIZE
        if keys[pygame.K_a]:
            offset.x -= 1*RESIZE

        screen.fill((0, 0, 255))
        for tile in tiles:
            tile.draw(offset)
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

        if pygame.Rect(500 * RESIZE, btn.y, btn.width, btn.height).collidepoint(mx, my):
            btn.x = btn.x + (550 * RESIZE - btn.x) * 0.1
            if click:
                state = "game"
        else:
            btn.x = btn.x + (500 * RESIZE - btn.x) * 0.1

        clock.tick(FPS)
        pygame.display.update()


main_menu()
