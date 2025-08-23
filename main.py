# TODO: game functions, snake body, highscore, score

from libs import *
from utils import *
from gfx import menu, map
from game import game

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
display.set_caption("Snake Game")

init()

menu()
game()

while True:
    close_window()