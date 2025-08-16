from libs import *
from utils import exit_game, text_font

header_size = 40
menu_size = 30

header_font = text_font(header_size)
menu_font = text_font(menu_size)

def rainbow_text(y, speed):
    for i in range(360):
        rgb = colorsys.hsv_to_rgb(i / 360, 1, 1)
        color = tuple(int(c * 255) for c in rgb)
        header = header_font.render("Snake Game", True, color)
        header_rect = header.get_rect(center=(screenSize[0] // 2, screenSize[1] // 2 + y))
        blit(header, header_rect)
        flip()
        time.wait(speed)
        exit_game()

def menu():
    def center(y):
        x = screenSize[0] // 2
        y += screenSize[1] // 2
        return (x, y)
    offset = 10
    menu_offset = menu_size + offset
    screen.fill((16, 16, 16))

    play = menu_font.render(">Play", True, (255, 255, 255))
    exit = menu_font.render("Exit", True, (255, 255, 255))

    play_rect = play.get_rect(center=center(0))
    exit_rect = exit.get_rect(center=center(30))

    blit(play, play_rect)
    blit(exit, exit_rect)
    flip()
    rainbow_text(-40, 5)