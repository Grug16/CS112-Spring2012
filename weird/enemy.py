"""  No need for ENV/BIN python because it's not going to be directly run.
enemy.py
badguys!
"""
import pygame
from pygame import Surface
from pygame.sprite import Sprite, Group #sprites and groups!

class Enemy (Sprite):
    size = 50, 30
    color = 255,0,0
    vx, vy, 6,6
    
    def __init__(self,bounds):
        Sprite.__init__(self)
        self.image = Surface(self.size)
        self.rect = self.image.get_rect()
        self.rect.bottomleft = loc
        
    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy