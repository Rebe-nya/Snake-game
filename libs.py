import pygame
from pygame import draw, font, display, time, display, QUIT, SYSTEM_CURSOR_HAND, SYSTEM_CURSOR_ARROW, MOUSEBUTTONDOWN
from pygame.draw import rect, ellipse, arc
from pygame.gfxdraw import arc
from pygame.display import flip, set_mode
from pygame.font import Font
from pygame.time import Clock
from pygame.mouse import get_pos, set_cursor, get_pressed
from os import path
from math import radians
import colorsys
import configparser
import math


clock = Clock()