import sys

import pygame.key

from levels import *


def main():
    level = load_level(BASE_WORLD)
    tiles, player = level

    offset = pygame.math.Vector2(0, 600)
    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                # stops player movement if player presses summoning button (k)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_k and player.grounded:
                    player.movable = not player.movable
                    player.vel.x = 0
        keys = pygame.key.get_pressed()
        player.update_pos(keys, tiles)

        #offset for camera control
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

        #maintians FPS of 30
        clock.tick(FPS)
        #updates the screen display every frame
        pygame.display.update()

#code for main menu
def main_menu():
    #creates starting button
    btn = pygame.Rect(300, 400, 100, 50)

    state = "game"

    #loop for game menu
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

            #calls game loop when the state is changed through buutton press
        if pygame.Rect(300, btn.y, btn.width, btn.height).collidepoint(mx, my):
            btn.x = btn.x + (350 - btn.x) * 0.1
            if click:
                state = "game"
        else:
            btn.x = btn.x + (300 - btn.x) * 0.1

        clock.tick(FPS)
        pygame.display.update()


main_menu()
