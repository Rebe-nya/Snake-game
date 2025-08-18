from libs import QUIT, pygame, display, time, set_mode

def text_font(size):
    return pygame.font.Font("fonts/04b_30/04B_30__.ttf", size)

def close_window():
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()

# Default values
screenSize = (800, 800)
fps = 60

screen = set_mode(screenSize)
blit = screen.blit