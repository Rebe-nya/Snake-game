from libs import pygame, QUIT, flip, time, clock
from utils import controls, fps
from gfx import map, map_x, map_y, num_sqr
#from main import fps
from snake import render_circle, game_grid

def game():
    # Start position
    x = 1
    y = 4

    grid = game_grid(0, 0)
    print(grid)
    print(map_y)
    loop = True
    while loop:
        clock.tick(fps)
        map()
        render_circle(x, y, 80)
        flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
                loop = False

        keys = pygame.key.get_pressed()
        if x > 0:
            if any(keys[key] for key in controls["left"]):
                x -= 1
        if x < num_sqr[0] - 1:
            if any(keys[key] for key in controls["right"]):
                x += 1
        if any(keys[key] for key in controls["up"]):
            if y > 0:
                y -= 1
        if any(keys[key] for key in controls["down"]):
            if y < num_sqr[1] - 1:
                y += 1

        time.wait(50)