#!/usr/bin/env python
import math

from random import randrange

import pygame
from pygame.locals import *
from pygame.sprite import Sprite, Group, RenderUpdates
import os, sys

C_BLACK = 0,0,0
class Game(object):
    
    title = "DrumKit"
    size = 800, 600
    fps = 30

    def __init__(self):
        self.screen = pygame.display.set_mode(self.size)
        self.bounds = self.screen.get_rect()
        pygame.display.set_caption(self.title)

    def run(self):
        clock = pygame.time.Clock()
        done = False
        while not done:
            # tick
            clock.tick(self.fps)

            # input
            for event in pygame.event.get():
                if event.type == QUIT:
                    done = True
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    done = True
                elif event.type == KEYDOWN and event.key == F:
                    PlayDrum()

            # update

            # draw
            self.screen.fill(C_BLACK)
            pygame.display.flip()

if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.run()
    print "Bye Bye"