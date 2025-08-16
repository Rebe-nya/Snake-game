import pygame
from pygame import rect, draw, font, display, time, display, event, QUIT
from os import path
import colorsys
import configparser

screenSize = (800, 800)
screen = display.set_mode(screenSize)
clock = time.Clock()
flip = display.flip
blit = screen.blit