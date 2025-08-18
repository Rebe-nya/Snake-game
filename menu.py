from libs import *
from utils import text_font, screenSize, screen, blit

def center(y):
    x = screenSize[0] // 2
    y += screenSize[1] // 2
    return (x, y)

def rainbow_text(speed, play_rect, exit_rect):
    for i in range(360):
        rgb = colorsys.hsv_to_rgb(i / 360, 1, 1)
        color = tuple(int(c * 255) for c in rgb)
        header = header_font.render("Snake Game", True, color)
        blit(header, header_rect)
        flip()

        if play_rect.collidepoint(get_pos()) or exit_rect.collidepoint(get_pos()):
            set_cursor(SYSTEM_CURSOR_HAND)
        else:
            set_cursor(SYSTEM_CURSOR_ARROW)
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if play_rect.collidepoint(event.pos):
                    print("Play clicked")
                if exit_rect.collidepoint(event.pos):
                    quit()
        time.wait(speed)

header_size = 40
menu_size = 30
header_font = text_font(header_size)
menu_font = text_font(menu_size)
offset = 15
offset = ((40 + 30 * 2)/3) + offset

play_text = "Play"
exit_text = "Exit"

play = menu_font.render(play_text, True, (255, 255, 255))
exit = menu_font.render(exit_text, True, (255, 255, 255))
header = header_font.render("Snake Game", True, (255, 255, 255))


header_rect = header.get_rect(center=center(-offset))
play_rect = play.get_rect(center=center(0))
exit_rect = exit.get_rect(center=center(offset))

def menu():
    screen.fill((16, 16, 16))
    blit(play, play_rect)
    blit(exit, exit_rect)
    flip()
    while True:
        rainbow_text(5, play_rect, exit_rect)