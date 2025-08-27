import pygame
from pygame import draw, font, display, time, display, QUIT, SYSTEM_CURSOR_HAND, SYSTEM_CURSOR_ARROW, MOUSEBUTTONDOWN, image, init, key
from pygame.draw import rect, ellipse, arc, polygon
from pygame.gfxdraw import arc, aacircle, filled_circle, aapolygon, filled_polygon
from pygame.display import flip, set_mode
from pygame.font import Font
from pygame.time import Clock
from pygame.mouse import get_pos, set_cursor, get_pressed
from os import path
from math import radians, floor
import colorsys
import configparser
import math

clock = Clock()