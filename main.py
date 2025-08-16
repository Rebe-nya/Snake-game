# TODO: config, center everything in menu, make selection in menu (on hover), game

from libs import pygame
pygame.init()

from libs import *
from utils import exit_game
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

def config():
    if not path.exists("config.ini"):
        with open("config.ini", "w") as configfile:
            config = configparser.ConfigParser()
            config["DEFAULT"] = {
            'screen_width': 800,
            'screen_height': 800,
            'fps': 60
        }
        config.write(configfile)
    else:
        config = configparser.ConfigParser()
        config.read("config.ini")

#map()

clock.tick(60)

while True:
    menu()
    exit_game()