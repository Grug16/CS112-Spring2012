#!/usr/bin/env python

import pygame
from pygame.locals import *

## COLORS
BLUE = 0, 133, 199
RED = 223, 0, 36
YELLOW = 244, 195, 0
GREEN = 0, 159, 61
BLACK = 0, 0, 0
WHITE = 255, 255, 255

THICKNESS = 20


## MAIN
pygame.init()
screen = pygame.display.set_mode((800, 388))
pygame.display.set_caption("Olympic Rings   [press ESC to quit]")
def degreeradian (deg):
    radians = deg/(180/3.14159)
    return radians
## Draw
screen.fill(WHITE)
# 240 apart horizontally.  110 radius, 20thick.
# for th
pygame.draw.circle(screen, BLUE, (160, 135), 110, 20)
pygame.draw.circle(screen, BLACK, (400, 135), 110, 20)
pygame.draw.circle(screen, RED, (640, 135), 110, 20)

pygame.draw.circle(screen, YELLOW, (280, 245), 110, 20)
pygame.draw.circle(screen, GREEN, (520, 245), 110, 20)

pygame.draw.arc(screen, WHITE, (50, 25, 225, 225), degreeradian(-20), degreeradian(10), 30)
pygame.draw.arc(screen, BLUE, (50, 25, 220, 220), degreeradian(-21), degreeradian(10), 20)

#Yellow
pygame.draw.arc(screen, WHITE, (165, 130, 225, 225), degreeradian(160), degreeradian(185), 30)
pygame.draw.arc(screen, YELLOW, (170, 135, 220, 220), degreeradian(159), degreeradian(185), 20)
pygame.draw.arc(screen, WHITE, (165, 130, 225, 225), degreeradian(60), degreeradian(90), 30)
pygame.draw.arc(screen, YELLOW, (170, 135, 220, 220), degreeradian(60), degreeradian(94), 20)


pygame.draw.arc(screen, WHITE, (290, 25, 225, 225), degreeradian(-20), degreeradian(10), 30)
pygame.draw.arc(screen, BLACK, (290, 25, 220, 220), degreeradian(-21), degreeradian(10), 20)
pygame.draw.arc(screen, WHITE, (290, 25, 225, 225), degreeradian(-120), degreeradian(-85), 30)
pygame.draw.arc(screen, BLACK, (290, 25, 220, 220), degreeradian(-120), degreeradian(-80), 20)

pygame.draw.arc(screen, WHITE, (530, 25, 225, 225), degreeradian(-20), degreeradian(10), 30)
pygame.draw.arc(screen, RED, (530, 25, 220, 220), degreeradian(-21), degreeradian(10), 20)
pygame.draw.arc(screen, WHITE, (530, 25, 225, 225), degreeradian(-120), degreeradian(-85), 30)
pygame.draw.arc(screen, RED, (530, 25, 220, 220), degreeradian(-120), degreeradian(-80), 20)

pygame.draw.arc(screen, WHITE, (405, 130, 225, 225), degreeradian(160), degreeradian(185), 30)
pygame.draw.arc(screen, GREEN, (410, 135, 220, 220), degreeradian(159), degreeradian(185), 20)
pygame.draw.arc(screen, WHITE, (405, 130, 225, 225), degreeradian(60), degreeradian(90), 30)
pygame.draw.arc(screen, GREEN, (410, 135, 220, 220), degreeradian(60), degreeradian(94), 20)


#################################
##  DRAW OLYPIC RINGS HERE
##
##  hint, lookup pygame.draw
##  specifically circle, ellipse,
##  and arc.  Also, the width
##  parameter
#################################


## Loop
clock = pygame.time.Clock()
done = False
while not done:
    event = pygame.event.poll()
    if event.type == QUIT:
        done = True
    elif event.type == KEYDOWN and event.key == K_ESCAPE:
        done = True

    pygame.display.flip()
    clock.tick(30)

print "ByeBye"
