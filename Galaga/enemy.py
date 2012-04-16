"""  No need for ENV/BIN python because it's not going to be directly run.
enemy.py
badguys!
"""
import pygame
from pygame import Surface
from pygame.sprite import Sprite, Group #sprites and groups!
from random import randrange

class Enemy (Sprite):
    size = 50, 30
    color = 255,0,0
    vx, vy = 6,6
    spawntime = 30
    spawnticker = 0
    
    def __init__(self,loc, bounds):
        Sprite.__init__(self)
        self.image = Surface(self.size)
        self.rect = self.image.get_rect()
        self.rect.bottomleft = loc
        self.image.fill(self.color)
        self.bounds = bounds
        self.vx = randrange(-6,6)
        self.vy = randrange(3,6)
        
        
    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        #spawn
        
        
        #bounce off side
        if self.rect.right > self.bounds.right or self.rect.left < self.bounds.left:
            self.vx *= -1
        
        
        #kill if out of bounds
        if self.rect.top > self.bounds.bottom:
            self.kill()
            
class FastEnemy(Enemy):
    color = 255,0,255
    size = 15,35
    def __init__(self, loc, bounds):
        Enemy.__init__(self, loc, bounds)
        
        self.vx = 0
        self.vy = 20
        
    
        