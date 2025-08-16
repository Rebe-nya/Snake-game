from libs import pygame, event, QUIT, font

def exit_game():
    for close in event.get():
        if close.type == QUIT:
            pygame.quit()
            exit()

def text_font(size):
    return pygame.font.Font("Fonts/04b_30/04B_30__.ttf", size)