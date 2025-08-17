# TODO: center everything in menu, offset, game

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

#map()
menu()