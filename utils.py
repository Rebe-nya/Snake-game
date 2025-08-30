from libs import QUIT, pygame, display, time, set_mode, font, path, configparser

# Default values
screenSize = (800, 800)
fps = 60

controls = {
    "up": [pygame.K_UP, pygame.K_w],
    "down": [pygame.K_DOWN, pygame.K_s],
    "left": [pygame.K_LEFT, pygame.K_a],
    "right": [pygame.K_RIGHT, pygame.K_d],
    "enter": [pygame.K_KP_ENTER]
}

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

def text_font(size):
    return font.Font("fonts/04b_30/04B_30__.ttf", size)

def close_window():
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()

def center(center_x, center_y):
    center_x += screenSize[0] // 2
    center_y += screenSize[1] // 2
    return (center_x, center_y)

screenSize, fps = config(screenSize, fps)
screen = display.set_mode(screenSize)
screen = set_mode(screenSize)
blit = screen.blit