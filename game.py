from libs import pygame, QUIT, flip, time, clock, key, floor, random
from utils import controls, fps
from gfx import map, num_sqr, apple
from snake import render_circle

def game():
    global x, y, direction, history
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
        
        for i in range(body_num):
            x1, y1 = history[i]
            render_circle(x1, y1, 80)
        for i in range(body_num):
            x1, y1 = history[i]
            render_circle(x1, y1, 80)

    def spawn_apple():
        global history
        apple_pos = (random.randint(0, num_sqr[0] - 1), random.randint(0, num_sqr[1] - 1))
        while apple_pos in history:
            apple_pos = (random.randint(0, num_sqr[0] - 1), random.randint(0, num_sqr[1] - 1))

        return apple_pos

    def apple_eaten():
        global apple_pos
        if apple_pos == (floor(x), floor(y)): return True
        else: return False

    running = True
    apple_pos = None
    while running:
        for event in pygame.event.get():
            if event.type == QUIT: running = False

        clock.tick(fps)

        print(history)

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
        if apple_pos == None:
            apple_pos = spawn_apple()
        print("apple:", apple_pos)

        map()
        apple(*apple_pos)
        move_snake(3)
        flip()

        time.wait(100)