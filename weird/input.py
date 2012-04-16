import pygame
from pygame.locals import *

class InputManager(object):
    def handle_event(event):
        if event.type == KEYDOWN and event.key == K_SPACE:
            print "Awesome Sauce"
        elif event.type == KEYDOWN and event.key == K_RETURN:
            print "With Fries"