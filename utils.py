from libs import QUIT, pygame, display, time, set_mode

def text_font(size):
    return pygame.font.Font("Fonts/04b_30/04B_30__.ttf", size)

# Default values
screenSize = (800, 800)
fps = 60

screen = set_mode(screenSize)
blit = screen.blit