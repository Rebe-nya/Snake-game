from libs import pygame, colorsys, get_pos, flip, set_cursor, SYSTEM_CURSOR_ARROW, SYSTEM_CURSOR_HAND, QUIT, MOUSEBUTTONDOWN, time, image, rect
from utils import text_font, screenSize, screen, blit, close_window, center

# Menu
def render_menu(speed, play_rect, exit_rect, header_font, header_rect, menu_font, play, exit, button_offset):
    for i in range(360):
        def render_text():
            screen.fill((16, 16, 16))
            blit(header, header_rect)
            blit(play, play_rect)
            blit(exit, exit_rect)
        def select(x, y):
            select = menu_font.render(">", True, (255, 255, 255))
            select_rect = select.get_rect(center=center(-x - 32, y))
            blit(select, select_rect)
        
        # Rainbow header
        rgb = colorsys.hsv_to_rgb(i / 360, 1, 1)
        color = tuple(int(c * 255) for c in rgb)
        header = header_font.render("Snake Game", True, color)

        # Selection symbol, cursor
        if play_rect.collidepoint(get_pos()):
            render_text()
            select(play_rect[3], 0)
            flip()
        elif exit_rect.collidepoint(get_pos()):
            render_text()
            select(exit_rect[3], button_offset)
            flip()
        else:
            render_text()
            flip()
        if play_rect.collidepoint(get_pos()) or exit_rect.collidepoint(get_pos()):
            set_cursor(SYSTEM_CURSOR_HAND)
        else:
            set_cursor(SYSTEM_CURSOR_ARROW)
        
        # Menu button functions
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if play_rect.collidepoint(event.pos):
                    set_cursor(SYSTEM_CURSOR_ARROW)

                    for opacity in range(0, 256, 8):
                        transparent_surface = pygame.Surface((screenSize[0], screenSize[1]), pygame.SRCALPHA)
                        transparent_surface.fill((0, 0, 0, opacity))
                        screen.blit(transparent_surface, (0, 0))
                        flip()
                        close_window()
                        time.wait(5)
                    return False
                if exit_rect.collidepoint(event.pos):
                    quit()
        time.wait(speed)
    return True

def menu():
    header_size = 40
    menu_size = 30
    header_font = text_font(header_size)
    menu_font = text_font(menu_size)
    play_text = "Play"
    exit_text = "Exit"
    button_offset = 15
    button_offset = ((40 + 30 * 2)/3) + button_offset

    play = menu_font.render(play_text, True, (255, 255, 255))
    exit = menu_font.render(exit_text, True, (255, 255, 255))
    header = header_font.render("Snake Game", True, (255, 255, 255))

    header_rect = header.get_rect(center=center(0, -button_offset))
    play_rect = play.get_rect(center=center(0, 0))
    exit_rect = exit.get_rect(center=center(0, button_offset))

    screen.fill((16, 16, 16))
    blit(header, header_rect)
    blit(play, play_rect)
    blit(exit, exit_rect)
    flip()

    while render_menu(play_rect=play_rect, exit_rect=exit_rect, header_font=header_font, header_rect=header_rect, speed=10, menu_font=menu_font, play=play, exit=exit, button_offset=button_offset):
        pass

# Game Map
map_rendered = False
top_bar_height = 80
map_offset = 100
num_sqr = [10, 10]
center_x, center_y = center(0, 0)

sqr_size_x = (screenSize[0] - map_offset) // num_sqr[0]
sqr_size_y = (screenSize[1] - map_offset - top_bar_height) // num_sqr[1]
if sqr_size_x < sqr_size_y:
    sqr_size = sqr_size_x
else:
    sqr_size = sqr_size_y

def top_bar(opacity, surface, top_bar_height):
    def icons():
        apple = image.load("assets/apple.png").convert_alpha()
        highscore = image.load("assets/highscore.png").convert_alpha()

        apple = pygame.transform.smoothscale(apple, (50, 50))
        highscore = pygame.transform.smoothscale(highscore, (50, 50))

        apple.set_alpha(opacity)
        highscore.set_alpha(opacity)

        apple_rect = apple.get_rect(center=(top_bar_height // 2, top_bar_height // 2))
        highscore_rect = highscore.get_rect(center=(top_bar_height // 2 + 125, top_bar_height // 2))

        surface.blit(apple, apple_rect)
        surface.blit(highscore, highscore_rect)

    surface.fill((74, 134, 45, opacity))
    rect(surface, (64, 115, 38, opacity), (0, 0, screenSize[0], top_bar_height))
    icons()

def map():
    global map_rendered

    def render_map(opacity):
        lightGreen = (121, 198, 83, opacity)
        darkGreen = (106, 191, 64, opacity)
        x = 0
        y = 0
        surface = pygame.Surface((screenSize[0], screenSize[1]), pygame.SRCALPHA)

        top_bar(opacity, surface, top_bar_height)
        for j in range(num_sqr[1]):
            for i in range(num_sqr[0]):
                x = i * sqr_size + center_x - (num_sqr[0] * sqr_size) / 2
                y = j * sqr_size + center_y - (num_sqr[1] * sqr_size) / 2 + top_bar_height / 2
                if (i + j) % 2 == 0:
                    rect(surface, lightGreen, (x, y, sqr_size, sqr_size))
                else:
                    rect(surface, darkGreen, (x, y, sqr_size, sqr_size))
                close_window()

        screen.blit(surface, (0, 0))

    if map_rendered:
        render_map(255)
    else:
        for opacity in range(0, 256, 8):
            render_map(opacity)
            flip()
            time.wait(5)
        map_rendered = True

# First square position
map_x = center_x - (num_sqr[0] * sqr_size) / 2
map_y = center_y - (num_sqr[1] * sqr_size) / 2 + top_bar_height / 2