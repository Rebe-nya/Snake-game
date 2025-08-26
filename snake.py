from libs import filled_circle, aacircle, filled_polygon, aapolygon
from utils import screen, close_window
from gfx import map_x, map_y, sqr_size

color = (0, 0, 255)

def game_grid(x, y):
    x = map_x + sqr_size / 2 + x * sqr_size
    y = map_y + sqr_size / 2 + y * sqr_size
    return x, y

def render_circle(x, y, size):
    size = (sqr_size / 2) * (size / 100)
    x, y = game_grid(x, y)
    size = round(size)
    filled_circle(screen, round(x), round(y), size, color)
    aacircle(screen, round(x), round(y), size, color)
    return size

def render_polygon(x1, y1, size1, x2, y2, size2):
    def position(x, y, size):
        x, y = game_grid(x, y)
        y = y - size
        return x, y
    x1, y1 = position(x1, y1, size1)
    x2, y2 = position(x2, y2, size2)
    points = [(x1, y1), (x1, y1 + size1 * 2), (x2, y2 + size2 * 2), (x2, y2)]
    filled_polygon(screen, points, color)
    aapolygon(screen, points, color)

"""
size1 = render_circle(0, 0, 80)
size2 = render_circle(9, 0, 40)
render_polygon(0, 0, size1, 9, 0, size2)
flip()

while True:
    close_window()
"""

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
