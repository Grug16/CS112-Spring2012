#!/usr/bin/env python

import math

from random import randrange

import pygame
from pygame.locals import *


## Settings
C_BLACK = 0,0,0
C_RED = 255,0,0


## from tiefighter.py
def draw_tie(surf, color, size):
    wall = size / 8

    surf.fill(C_BLACK)
    pygame.draw.rect(surf, color, (0, 0, wall, size))
    pygame.draw.rect(surf, color, (size-wall, 0, wall, size))
    pygame.draw.rect(surf, color, (0, (size-wall)/2, size, wall))
    pygame.draw.circle(surf, color, (size/2, size/2), size/4)

class TieFighter(object):
    def __init__(self, x, y, vx, vy, size = 40, color = C_RED):
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
        self.size = size
        self.color = color
        self.image = pygame.surface((size,size))
        draw_tie(self.image,color,size)
        self.rect=pygame.Rect(x,y,size,size)
    
    def draw(self, surf):
        surface.blit(self.image, self.rect)


class Game(object):
    title = "Tie Hunt"
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

            # update

            # draw
            self.screen.fill(C_BLACK)
            pygame.display.flip()



if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.run()
    print "Bye Bye"
