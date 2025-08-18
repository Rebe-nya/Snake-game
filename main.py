# TODO: game

from libs import pygame
pygame.init()

from libs import *
from utils import *
from menu import menu

def map():
    lightGreen = (0, 200, 0)
    darkGreen = (0, 150, 0)
    sqr = 50

    for j in range(screenSize[1] // 50):
        for i in range(screenSize[0] // 50):
            x = i * sqr
            y = j * sqr

            if (i + j) % 2 == 0:
                rect(screen, lightGreen, (x, y, sqr, sqr))
            else:
                rect(screen, darkGreen, (x, y, sqr, sqr))
    flip()

def config(screenSize, fps):
    if not path.exists("config.ini"):
        config = configparser.ConfigParser()
        config["Settings"] = {
            'screen_width': screenSize[0],
            'screen_height': screenSize[1],
            'fps': fps
        }
        with open("config.ini", "w") as configfile:
            config.write(configfile)
    config = configparser.ConfigParser()
    config.read("config.ini")

    screenSize = (
        config.getint("Settings", "screen_width"),
        config.getint("Settings", "screen_height")
    )
    fps = config.getint("Settings", "fps")
    return screenSize, fps

screenSize, fps = config(screenSize, fps)
screen = display.set_mode(screenSize)
clock.tick(fps)

#menu()

"""
map()
ellipse(screen, (0, 0, 255), (5, 5, 40, 40))
ellipse(screen, (255, 0, 0), (55, 5, 40, 40))
rect(screen, (255, 0, 0), (25, 5, 55, 40))
flip()

time.wait(2000)
map()
ellipse(screen, (255, 0, 0), (5, 5, 40, 40))
flip()
"""

map()
ellipse(screen, (0, 0, 255), (5 + 0 * 50, 5, 40, 40))
ellipse(screen, (0, 0, 255), (55 + 0 * 50, 5, 40, 40))
rect(screen, (0, 0, 255), (25 + 0 * 50, 5, 55, 40))
ellipse(screen, (0, 0, 255), (5 + 0 * 50, 55, 40, 40))
rect(screen, (0, 0, 255), (5 + 0 * 50, 25, 40, 55))

"""
arc(
    screen,
    (0, 0, 255),
    (40, 40, 40, 40),  # rect: x, y, w, h
    radians(90),              # start_angle
    radians(180),              # end_angle
    5                              # tloušťka oblouku (např. 8 pixelů)
)
arc(
    screen,
    (0, 0, 255),
    (100, 100, 45, 45),  # rect: x, y, w, h
    radians(90),              # start_angle
    radians(180),              # end_angle
    5                              # tloušťka oblouku (např. 8 pixelů)
)
"""
for position in range(11):
    arc(screen, 55 - position, 55 - position, 10 - position, 180, 270, (0, 0, 255))
flip()

"""
    arc(screen, 45 - i, 45 - i, 50, 90, 180, (0, 0, 255))

    time.wait(100)
"""

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()