import pygame

pygame.init()

screenSize = (800, 800)
screen = pygame.display.set_mode(screenSize)
clock = pygame.time.Clock()
draw = pygame.draw
rect = draw.rect
flip = pygame.display.flip

def map():
    lightGreen = (0, 200, 0)
    darkGreen = (0, 150, 0)
    sqr = 50

    for j in range(screenSize[1] // 50):
        for i in range(screenSize[0] // 50):
            x = i * sqr
            y = j * sqr

            if (i + j) % 2 == 0:
                rect(screen, lightGreen, (x, y, sqr, sqr))
            else:
                rect(screen, darkGreen, (x, y, sqr, sqr))

clock.tick(60)
map()

font = pygame.font.Font("Fonts/04b_30/04B_30__.ttf", 32)
text = font.render("Snake Game", True, (255, 255, 255))
screen.blit(text, (screenSize[0] // 2 - text.get_width() // 2, screenSize[1] // 2 - text.get_height() // 2))
flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()