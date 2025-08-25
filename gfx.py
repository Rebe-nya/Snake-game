from libs import pygame, colorsys, get_pos, flip, set_cursor, SYSTEM_CURSOR_ARROW, SYSTEM_CURSOR_HAND, QUIT, MOUSEBUTTONDOWN, time, image, rect
from utils import text_font, screenSize, screen, blit, close_window, center

# Menu
def menu_render(speed, play_rect, exit_rect, header_font, header_rect, menu_font, play, exit, button_offset):
    for i in range(360):
        def text_render():
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
            text_render()
            select(play_rect[3], 0)
            flip()
        elif exit_rect.collidepoint(get_pos()):
            text_render()
            select(exit_rect[3], button_offset)
            flip()
        else:
            text_render()
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

    while menu_render(play_rect=play_rect, exit_rect=exit_rect, header_font=header_font, header_rect=header_rect, speed=10, menu_font=menu_font, play=play, exit=exit, button_offset=button_offset):
        pass

# Game Map
map_rendered = False

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
        
    center_x, center_y = center(0, 0)
    num_x_sqr = 10
    num_y_sqr = 10
    sqr_size = 60
    top_bar_height = 80

    def map_render(opacity):
        lightGreen = (121, 198, 83, opacity)
        darkGreen = (106, 191, 64, opacity)
        x = 0
        y = 0
        surface = pygame.Surface((screenSize[0], screenSize[1]), pygame.SRCALPHA)

        top_bar(opacity, surface, top_bar_height)
        for j in range(num_y_sqr):
            for i in range(num_x_sqr):
                x = i * sqr_size + center_x - (num_x_sqr * sqr_size) // 2
                y = j * sqr_size + center_y - (num_y_sqr * sqr_size) // 2 + top_bar_height // 2
                if (i + j) % 2 == 0:
                    rect(surface, lightGreen, (x, y, sqr_size, sqr_size))
                else:
                    rect(surface, darkGreen, (x, y, sqr_size, sqr_size))
                close_window()

        screen.blit(surface, (0, 0))
        flip()

    if map_rendered:
        map_render(255)
    else:
        for opacity in range(0, 256, 8):
            map_render(opacity)
            time.wait(5)
        map_rendered = True

    map_x = center_x - (num_x_sqr * sqr_size) // 2
    map_y = center_y - (num_y_sqr * sqr_size) // 2 + top_bar_height // 2
    return map_x, map_y, num_x_sqr, num_y_sqr, sqr_size