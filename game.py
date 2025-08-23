from libs import *
from utils import controls
from gfx import map

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