"""  No need for ENV/BIN python because it's not going to be directly run.
player.py
player class for our shmup
"""
import pygame
from pygame import Surface
from pygame.sprite import Sprite, Group #sprites and groups!

class Player (Sprite):
    size = 20,20
    color = 255,255,0
    shottimer = 0
    
    def __init__(self, loc, bounds):
        Sprite.__init__(self)  # required for sprites
        self.image = Surface(self.size)
        self.rect = self.image.get_rect()
        
        self.rect.center = loc
        self.bounds = bounds  # passes the bounds to the object so it can be saved.
        
        self.image.fill(self.color)
        self.bullets = Group()
    
    def update(self):
        if self.shottimer > 0:
            self.shottimer -= 1
        self.rect.center = pygame.mouse.get_pos()
        self.rect.clamp_ip(self.bounds) #makes sure it doesn't go outside the provided rectangle
        
    def shoot(self):
        if not self.alive(): #return just stops everything in hte function
            return
        if self.shottimer == 0:
            bullet = Bullet(self.bounds)
            self.bullets.add(bullet) #adds the new bullet to the Bullets list
        
            bullet.rect.midbottom = self.rect.midtop
            self.shottimer = 10
        
        
class Bullet(Sprite):
    size = 5, 10
    color = 0, 200, 60
    speed = 7
    def __init__(self, bounds):
        Sprite.__init__(self)
        
        self.image = Surface (self.size)
        self.rect = self.image.get_rect()
        self.bounds = bounds
        self.image.fill(self.color)
    
    def update(self):
        self.rect.y -= self.speed
        if self.rect.top <= self.bounds.top:
            self.kill() #kill deletes sprites
        
        
        
        