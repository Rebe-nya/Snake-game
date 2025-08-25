from libs import *
from utils import screen, close_window
from gfx import map

def circle_render(x, y, size):
    size = (sqr_size // 2) * (size / 100)
    x = map_x + sqr_size / 2 + x * sqr_size
    y = map_y + sqr_size / 2 + y * sqr_size
    #print("Map:", map_x, map_y, sqr_size)
    #print("Circle:", x, y, size * 2)
    size = round(size)
    filled_circle(screen, round(x), round(y), size, color)
    aacircle(screen, round(x), round(y), size, color)
    return size

def polygon_render(x1, y1, size1, x2, y2, size2):
    def position(x, y, size):
        x = map_x + sqr_size // 2 + x * sqr_size
        y = map_y + sqr_size // 2 - size + y * sqr_size
        return x, y
    x1, y1 = position(x1, y1, size1)
    x2, y2 = position(x2, y2, size2)
    points = [(x1, y1), (x1, y1 + size1 * 2), (x2, y2 + size2 * 2), (x2, y2)]
    filled_polygon(screen, points, color)
    aapolygon(screen, points, color)

map_x, map_y, num_x_sqr, num_y_sqr, sqr_size = map()
color = (0, 0, 255)

size1 = circle_render(0, 0, 80)
size2 = circle_render(9, 0, 40)
polygon_render(0, 0, size1, 9, 0, size2)
flip()

'''
def circle_body(x1, y1, size1, x2, y2, size2):
    x2 = x2 * 10
    for i in range(x1, x2, 1):
        temp = x1 + i / 10
        size = size1 - (size1 - size2) * (i / 10)
        print(size1, size2)
        print(size)
        circle_render(temp, y1, size)

# Turn arc
for position in range(6):
    arc(screen, 50 - position, 50 - position, 5 - position, 180, 270, (0, 0, 255))
flip()
'''

while True:
    close_window()