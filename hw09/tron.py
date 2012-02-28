#!/usr/bin/env python
"""
tron.py

The simple game of tron with two players.  Press the space bar to start the game.  Player 1 (red) is controlled with WSAD and player 2 (blue) is controlled with the arrow keys.  Once the game is over, press space to reset and then again to restart.  Escape quits the program.
"""

import pygame
from pygame import draw
from pygame.locals import *


def draw1(pos):
    x,y = pos
    draw.rect(screen, red, (x, y, 5, 5))
    
def draw2(pos):
    x,y = pos
    draw.rect(screen, blue, (x, y, 5, 5))

#coordinates of players
p1x,p1y = 0,0
p2x,p2y = 0,0

#player heading/direction
p1dx,p1dy = 0,0
p2dx,p2dy = 0,0

p1score = 0
p2score = 0

def move(x, y, dx, dy, edges):
    x+=dx
    y+=dy
    
    if x<edges.left or x>edges.right or y<edges.top or y>edges.bottom:
        dx = 0
        dy = 0
        
        y=-5
        x=-5
    
    return x, y, dx, dy



black = 0,0,0
red = 255,28,174
blue = 135,206,255
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Welcome to Tron - Press Space to Begin.")
clock = pygame.time.Clock()
done = False
play = False
p1pos = []
p2pos = []
p1tail = []
p2tail = []
screen_edge = screen.get_rect()
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True
        elif event.type == KEYDOWN and event.key == K_SPACE:
            play = True
            del p1tail[:]
            del p2tail[:]
            p1dx,p1dy=2,0
            p1x,p1y = 100,300
            p2dx,p2dy=-2,0
            p2x,p2y = 700,300
    
    if play:
        # player 1
        if event.type == KEYDOWN and event.key == K_w and p1dy != 2:
            p1dx, p1dy = 0,-2 #up
        elif event.type == KEYDOWN and event.key == K_s and p1dy != -2:
            p1dx, p1dy = 0,2 #down
        elif event.type == KEYDOWN and event.key == K_d and p1dx != -2:
            p1dx, p1dy = 2,0 #right
        elif event.type == KEYDOWN and event.key == K_a and p1dx != 2:
            p1dx, p1dy = -2,0 #left
        
        #player 2
        elif event.type == KEYDOWN and event.key == K_UP and p2dy != 2:
            p2dx, p2dy = 0,-2
        elif event.type == KEYDOWN and event.key == K_RIGHT and p2dx != -2:
            p2dx, p2dy = 2,0
        elif event.type == KEYDOWN and event.key == K_DOWN and p2dy != -2:
            p2dx, p2dy = 0,2
        elif event.type == KEYDOWN and event.key == K_LEFT and p2dx != 2:
            p2dx, p2dy = -2,0
       
        screen.fill(black)
        
        p1x, p1y, p1dx, p1dy = move(p1x, p1y, p1dx, p1dy, screen_edge)
        p2x, p2y, p2dx, p2dy = move(p2x, p2y, p2dx, p2dy, screen_edge)
        
        p1tail.append([p1x, p1y])
        p2tail.append([p2x, p2y])
        
        p1pos.append([p1x, p1y])
        p2pos.append([p2x, p2y])
        
        for i in range(len(p1tail)):
            draw1(p1tail[i])
        for i in range(len(p2tail)):
            draw2(p2tail[i])
        
        if (p1pos[-1] in p1tail[:-1]) or (p1pos[-1] in p2tail[:-1]):
            play = False
            dx=0 #movement halts

            dy=0
            p2score +=1

            print "Player 2 wins."
            print " Player 1:", p1score,"\n Player 2:", p2score 
            
        elif (p2pos[-1] in p2tail[:-1]) or (p2pos[-1] in p1tail[:-1]):
            play = False
            dx = 0
            dy = 0
            p1score+=1

            print "Player 1 wins."
            print " Player 1:", p1score,"\n Player 2:", p2score

    pygame.display.flip()   
    clock.tick(60)
