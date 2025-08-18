from libs import *
from utils import screen

"""
map()
ellipse(screen, (0, 0, 255), (5, 5, 40, 40))
ellipse(screen, (255, 0, 0), (55, 5, 40, 40))
rect(screen, (255, 0, 0), (25, 5, 55, 40))
flip()

time.wait(2000)
map()
ellipse(screen, (255, 0, 0), (5, 5, 40, 40))
flip()
"""

ellipse(screen, (0, 0, 255), (5 + 0 * 50, 5, 40, 40))
ellipse(screen, (0, 0, 255), (55 + 0 * 50, 5, 40, 40))
rect(screen, (0, 0, 255), (25 + 0 * 50, 5, 55, 40))
ellipse(screen, (0, 0, 255), (5 + 0 * 50, 55, 40, 40))
rect(screen, (0, 0, 255), (5 + 0 * 50, 25, 40, 55))

# Turn arc
for position in range(6):
    arc(screen, 50 - position, 50 - position, 5 - position, 180, 270, (0, 0, 255))
flip()