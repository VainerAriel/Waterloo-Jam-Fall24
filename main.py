import sys

import pygame.key

from levels import *


def main():
    level = load_level(BASE_WORLD)
    tiles, movable_tiles, player = level

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                # stops player movement if player presses summoning button (k)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_k and player.grounded:
                    if not player.creature:
                        summon_tile = player.check_tile_nearby(BASE_WORLD, movable_tiles)
                        if summon_tile is not None:
                            player.summon(summon_tile)
                    else:
                        player.creature.vel.x = 0

                    player.vel.x = 0
                    player.controlling_player = not player.controlling_player

                if event.key == pygame.K_SPACE:
                    if not player.controlling_player and player.creature:
                        if player.creature.box_picked is None:
                            player.creature.pickup(tiles)
                        else:
                            player.creature.box_picked.picked_up = False
                            player.creature.box_picked.drop = True
                            player.creature.box_picked = None


        keys = pygame.key.get_pressed()
        player.update(keys, tiles, clock.get_time())

        # offset for camera control
        camera_offset = player.offset.copy()
        if not player.controlling_player and player.creature:
            camera_offset = player.creature.offset.copy()

        new_offset = pygame.math.Vector2(player.rect.x - 800 * WIDTH / 1920, player.rect.y - 600 * WIDTH / 1920)
        if not player.controlling_player and player.creature:
            new_offset = pygame.math.Vector2(player.creature.rect.x - 800 * WIDTH / 1920,
                                             player.creature.rect.y - 600 * WIDTH / 1920)

        if 0 <= new_offset.x <= SCALE * 12 and 0 <= new_offset.y <= SCALE * 10:
            camera_offset = new_offset.copy()
        elif 0 <= new_offset.x <= SCALE * 12:
            camera_offset.x = new_offset.x
        elif 0 <= new_offset.y <= SCALE * 10:
            camera_offset.y = new_offset.y

        for tile in tiles:
            if not tile.movable:
                tile.draw(camera_offset)

        for tile in tiles:
            if tile.movable:
                tile.update_movable_tile(tiles, player)
                tile.draw(camera_offset)

        player.draw(camera_offset)
        for i in range(grid_w):
            for j in range(grid_h):
                pygame.draw.rect(screen, (100, 100, 100), (i * SCALE - camera_offset.x, j * SCALE - camera_offset.y, SCALE, SCALE), 2)

        if not player.controlling_player and player.creature:
            player.creature.offset = camera_offset.copy()
        else:
            player.offset = camera_offset.copy()
        # maintians FPS of 30
        clock.tick(FPS)
        # updates the screen display every frame
        pygame.display.update()


# code for main menu
def main_menu():
    # creates starting button
    btn = pygame.Rect(300, 400, 100, 50)

    state = "game"

    # loop for game menu
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

            # calls game loop when the state is changed through button press
        if pygame.Rect(300, btn.y, btn.width, btn.height).collidepoint(mx, my):
            btn.x = btn.x + (350 - btn.x) * 0.1
            if click:
                state = "game"
        else:
            btn.x = btn.x + (300 - btn.x) * 0.1

        clock.tick(FPS)
        pygame.display.update()


main_menu()
