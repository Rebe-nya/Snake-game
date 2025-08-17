import pygame
from pygame import draw, font, display, time, display, QUIT, SYSTEM_CURSOR_HAND, SYSTEM_CURSOR_ARROW, MOUSEBUTTONDOWN
from pygame.draw import rect
from pygame.display import flip, set_mode
from pygame.font import Font
from pygame.time import Clock
from pygame.mouse import get_pos, set_cursor, get_pressed
from os import path
import colorsys
import configparser

clock = Clock()