#!/usr/bin/env python
import pygame
#required for pygame
from pygame import gfxdraw
from pygame.locals import *
# loads pygame shortcuts like QUIT, KEYDOWN, and such.

SCREEN_SIZE=640,480
FPS = 30

screen = None
player = Rect(0,0,16,16)
bounds = Rect(0,0,200,200)


def center_mouse():
    x,y = screen.get_rect().center
    pygame.mouse.set_pos(x,y)
    pygame.mouse.get_pos()


def update():
    player.center = pygame.mouse.get_pos()
    player.clamp_ip(bounds)
    if not bounds.contains(player):
        player.center = bounds.center


def draw(surf):
    surf.fill((80,80,80))
    surf.fill((0,0,0), bounds)
    surf.fill((255,0,0), player)
    
  #  x,y = pygame.mouse.get_pos()
 #   gfxdraw.filled_circle(surf, x, y, 8, (0,0,0))
  #  gfxdraw.filled_circle(surf, x, y, 5, (255,0,0))
    
    


def run():
    global screen
    
    pygame.init() #starts pygame.  Initialize.
    screen = pygame.display.set_mode(SCREEN_SIZE, DOUBLEBUF|HWSURFACE) #creates the screen.  Set_Mode is required.
    #pygame.mouse.set_visible(False)
    clock = pygame.time.Clock() # Involves game time, not real time.  Tick is important.
    
    #center the bounds
    bounds.center = screen.get_rect().center
    
    #center the mouse
    center_mouse()
   
    
    #Game loop
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == QUIT:
                done = true
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                done = true
        
        update()
        draw(screen)
        clock.tick(FPS) #Tick makes it not go faster than FPS
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    run()
    print "ByeBye" #To show that pygame quit properly.