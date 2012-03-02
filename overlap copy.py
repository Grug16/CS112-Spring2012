#!/usr/bin/env python

import pygame
from pygame.locals import *

## Settings
BACKGROUND = 80,80,80
RED = 255,0,0
WHITE = 255,255,255
GREEN = 0,255,0

SCREEN_SIZE = 800,600
RECT_SIZE = 120,80
FPS = 30

## initialize
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

## setup game objects
bounds = screen.get_rect()

rects = [ pygame.Rect((0,0), RECT_SIZE),
          pygame.Rect((0,0), RECT_SIZE),
          pygame.Rect((0,0), RECT_SIZE),
          pygame.Rect((0,0), RECT_SIZE) ]

rects[0].topleft = bounds.topleft
rects[1].topright = bounds.topright
rects[2].bottomleft = bounds.bottomleft
rects[3].bottomright = bounds.bottomright

bigfont = pygame.font.Font(None, 80)

## game loop
clock = pygame.time.Clock()
done = False
grabbed = False
while not done:
    # input
    for evt in pygame.event.get():
        # quit
        if evt.type == QUIT:
            done = True
        elif evt.type == KEYDOWN and evt.key == K_ESCAPE:
            done = True
        # grab rect
        elif evt.type == MOUSEBUTTONDOWN:
            # find grabbed rect
            for rect in rects:
                if rect.collidepoint(pygame.mouse.get_pos()):
                    grabbed = rect

            # move grabbed rect to the top
            if grabbed:
                rects.remove(grabbed)
                rects.append(grabbed)

        elif evt.type == MOUSEBUTTONUP:
            grabbed = None

    # update
    if grabbed:
        grabbed.center = pygame.mouse.get_pos()
        grabbed.clamp_ip(bounds)

    # draw
    screen.fill(BACKGROUND)
    
    # instructions
    text = bigfont.render("Drag the rectangles", True, (0,0,0), BACKGROUND)
    loc = text.get_rect()
    loc.center = bounds.center
    screen.blit(text, loc)

    for rect in rects:
        others = rects[:]
        others.remove(rect)

        if rect == grabbed:
            color = WHITE
        elif rect.collidelist(others) != -1:
            color = GREEN
        else:
            color = RED

        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, (0,0,0), rect, 5)

    # refresh
    pygame.display.flip()
    clock.tick(FPS)








