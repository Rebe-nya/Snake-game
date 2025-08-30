from libs import pygame, QUIT, flip, time, clock, key, floor
from libs import pygame, QUIT, flip, time, clock, key, floor
from utils import controls, fps
from gfx import map, num_sqr
from snake import render_circle
from gfx import map, num_sqr
from snake import render_circle

def game():
    global x, y, direction
    x, y = 1.0, 4.0
    speed = 1
    history = [(x - 1, y), (x, y), (x + 1, y)]
    direction = None

    def move_snake(body_num):
        global x, y, direction

        if direction != None:
            if direction == "left" and x > 0: x -= 1
            elif direction == "right" and x < num_sqr[0] - 1: x += 1
            elif direction == "up" and y > 0: y -= 1
            elif direction == "down" and y < num_sqr[1] - 1: y += 1
            history.append((x, y))
            history.pop(0)

        if (x, y) != history[-1]: history.append((x, y))
        if len(history) > body_num: history.pop(0)
        
    global x, y, direction
    x, y = 1.0, 4.0
    speed = 1
    history = [(x - 1, y), (x, y), (x + 1, y)]
    direction = None

    def move_snake(body_num):
        global x, y, direction

        if direction != None:
            if direction == "left" and x > 0: x -= 1
            elif direction == "right" and x < num_sqr[0] - 1: x += 1
            elif direction == "up" and y > 0: y -= 1
            elif direction == "down" and y < num_sqr[1] - 1: y += 1
            history.append((x, y))
            history.pop(0)

        if (x, y) != history[-1]: history.append((x, y))
        if len(history) > body_num: history.pop(0)
        
        map()
        for i in range(body_num):
            x1, y1 = history[i]
            render_circle(x1, y1, 80)
        for i in range(body_num):
            x1, y1 = history[i]
            render_circle(x1, y1, 80)
        flip()

    running = True
    while running:
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                running = False

        print(history)

        clock.tick(fps)

        for i in range(speed * 100):
            keys = key.get_pressed()
        print(history)

        clock.tick(fps)

        for i in range(speed * 100):
            keys = key.get_pressed()
            if any(keys[key] for key in controls["left"]):
                direction = "left"
            elif any(keys[key] for key in controls["right"]):
                direction = "right"
            elif any(keys[key] for key in controls["up"]):
                direction = "up"
            elif any(keys[key] for key in controls["down"]):
                direction = "down"

        move_snake(3)

        time.wait(100)