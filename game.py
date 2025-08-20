from libs import *
from gfx import map

controls = {
    "up": [pygame.K_UP, pygame.K_w],
    "down": [pygame.K_DOWN, pygame.K_s],
    "left": [pygame.K_LEFT, pygame.K_a],
    "right": [pygame.K_RIGHT, pygame.K_d]
}

def game():
    num_x, num_y = map()
    print(f"Map created with {num_x} squares in X and {num_y} squares in Y.")
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key in controls["up"]:
                    print("Moving up")
                elif event.key in controls["down"]:
                    print("Moving down")
                elif event.key in controls["left"]:
                    print("Moving left")
                elif event.key in controls["right"]:
                    print("Moving right")