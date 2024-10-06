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
                if event.key == pygame.K_l and player.grounded and player.creature and not player.summoning:
                    player.summoning =True
                    player.controlling_player = False
                    player.creature.update_timer(99999999)
                if event.key == pygame.K_k and player.grounded and not player.summoning:
                    if  player.creature == None:
                        player.controlling_player = True
                        player.summoning = True
                        summon_tile = player.check_tile_nearby(BASE_WORLD, movable_tiles)
                        if summon_tile is not None:
                            player.summon(summon_tile)
                    else:
                        player.creature.vel.x = 0
                        player.controlling_player = not player.controlling_player
                    player.vel.x = 0

                if event.key == pygame.K_SPACE:
                    if not player.controlling_player and player.creature and player.creature.carrying_block == False:
                        print(len(player.creature.stack))
                        if len(player.creature.stack) == 0:
                            player.creature.pickup(tiles, movable_tiles, BASE_WORLD, player)
                            player.creature.carrying_block = True
                        else:
                            for box in player.creature.stack:
                                box.picked_up = False
                                box.drop = True
                            player.creature.stack = []



        keys = pygame.key.get_pressed()
        player.update(keys, tiles, clock.get_time())

        # offset for camera control
        camera_offset = player.offset.copy()
        if not player.controlling_player and player.creature:
            camera_offset = player.creature.offset.copy()

        new_offset = pygame.math.Vector2(player.rect.x - WIDTH/2, player.rect.y-HEIGHT/2)
        if not player.controlling_player and player.creature:
            new_offset = pygame.math.Vector2(player.creature.rect.x - WIDTH/2,
                                             player.creature.rect.y - HEIGHT/2)

        if 0 <= new_offset.x <= grid_w*SCALE - WIDTH and 0 <= new_offset.y <= grid_h*SCALE - HEIGHT:
            camera_offset = new_offset.copy()
        elif 0 <= new_offset.x <= grid_w*SCALE - WIDTH:
            camera_offset.x = new_offset.x
        elif 0 <= new_offset.y <= grid_h*SCALE - HEIGHT:
            camera_offset.y = new_offset.y

        image(screen, bg, (0-camera_offset.x, 0-camera_offset.y))

        for tile in tiles:
            if not tile.movable:
                tile.draw(camera_offset)

        for tile in tiles:
            if tile.movable:
                tile.update_movable_tile(tiles, player)
                tile.draw(camera_offset)

        player.draw(camera_offset)
        # for i in range(grid_w):
        #     for j in range(grid_h):
        #         pygame.draw.rect(screen, (100, 100, 100), (i * SCALE - camera_offset.x, j * SCALE - camera_offset.y, SCALE, SCALE), 2)

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
