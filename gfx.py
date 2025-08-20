from libs import *
from utils import text_font, screenSize, screen, blit, close_window

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

        rgb = colorsys.hsv_to_rgb(i / 360, 1, 1)
        color = tuple(int(c * 255) for c in rgb)
        header = header_font.render("Snake Game", True, color)

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

def center(x, y):
    x += screenSize[0] // 2
    y += screenSize[1] // 2
    return (x, y)

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
def map():
    screen.fill((16, 16, 16))
    offset = 40
    sqr = 40
    for opacity in range(0, 256, 8):
        surface = pygame.Surface((screenSize[0], screenSize[1]), pygame.SRCALPHA)
        frame_height = frame(opacity, surface)
        lightGreen = (121, 198, 83, opacity)
        darkGreen = (106, 191, 64, opacity)
        num_x_sqr = 0
        num_y_sqr = 0
        for j in range(((screenSize[1] - offset - frame_height) // sqr) - offset // sqr):
            num_y_sqr += 1
            for i in range(((screenSize[0] - offset) // sqr) - offset // sqr):
                num_x_sqr += 1
                x = i * sqr + offset
                y = j * sqr + frame_height + offset
                if (i + j) % 2 == 0:
                    rect(surface, lightGreen, (x, y, sqr, sqr))
                else:
                    rect(surface, darkGreen, (x, y, sqr, sqr))
                close_window()
        screen.blit(surface, (0, 0))
        flip()
        time.wait(5)
    num_x_sqr = num_x_sqr // num_y_sqr
    return num_x_sqr, num_y_sqr
    
def frame(opacity, surface):
    def icons():
        apple = image.load("assets/apple.png").convert_alpha()
        highscore = image.load("assets/highscore.png").convert_alpha()

        apple = pygame.transform.smoothscale(apple, (50, 50))
        highscore = pygame.transform.smoothscale(highscore, (50, 50))

        apple.set_alpha(opacity)
        highscore.set_alpha(opacity)

        apple_rect = apple.get_rect(center=(height // 2, height // 2))
        highscore_rect = highscore.get_rect(center=(height // 2 + 125, height // 2))

        surface.blit(apple, apple_rect)
        surface.blit(highscore, highscore_rect)

    height = 80
    surface.fill((74, 134, 45, opacity))
    rect(surface, (64, 115, 38, opacity), (0, 0, screenSize[0], height))
    icons()
    return height



