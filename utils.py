from libs import QUIT, pygame, display, time, set_mode

controls = {
    "up": [pygame.K_UP, pygame.K_w],
    "down": [pygame.K_DOWN, pygame.K_s],
    "left": [pygame.K_LEFT, pygame.K_a],
    "right": [pygame.K_RIGHT, pygame.K_d],
    "enter": [pygame.K_KP_ENTER]
}

def text_font(size):
    return pygame.font.Font("fonts/04b_30/04B_30__.ttf", size)

def close_window():
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()

def center(center_x, center_y):
    center_x += screenSize[0] // 2
    center_y += screenSize[1] // 2
    return (center_x, center_y)


# Default values
screenSize = (800, 800)
fps = 60

screen = set_mode(screenSize)
blit = screen.blit