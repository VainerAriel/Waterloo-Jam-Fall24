import sys

import pygame.key

from levels import *


def main():
    level = load_level(BASE_WORLD)
    tiles, player = level

    offset = pygame.math.Vector2(0, 600)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        player.update_pos(keys, tiles)
        new_offset = pygame.math.Vector2(player.pos.x - 800*WIDTH/1920, player.pos.y - 600*WIDTH/1920)
        if 0 <= new_offset.x <= SCALE * 12 and 0 <= new_offset.y <= SCALE * 10:
            offset = new_offset
        elif 0 <= new_offset.x <= SCALE * 12:
            offset.x = new_offset.x
        elif 0 <= new_offset.y <= SCALE * 10:
            offset.y = new_offset.y
        screen.fill((0, 0, 255))
        for tile in tiles:
            tile.draw(offset)
        player.draw(offset)

        clock.tick(FPS)
        pygame.display.update()


def main_menu():
    btn = pygame.Rect(300, 400, 100, 50)

    state = "game"

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

        if pygame.Rect(300, btn.y, btn.width, btn.height).collidepoint(mx, my):
            btn.x = btn.x + (350 - btn.x) * 0.1
            if click:
                state = "game"
        else:
            btn.x = btn.x + (300 - btn.x) * 0.1

        clock.tick(FPS)
        pygame.display.update()


main_menu()
