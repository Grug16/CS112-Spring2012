#!/usr/bin/env python

import pygame
from pygame.locals import *

#This is how you import stuff
from core.input import InputManager, KeydownListener


class Player(object):
    def move (self, direction):
        print "player moves %d,%d" % direction
    def jump(self):
        print "player jumps"

class SoundManager(object):
    def play(self, which):
        print "playing %s sound" % which

class PlayerController(KeydownListener):
    def __init__(self, player):
        self.player = player
        
    def on_keydown(self,event):
        self.player.jump()

class Game(object):
    size = 800,600
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        
        self.input = InputManager()
        
        self.player = Player()
        
        self.input.add_listener(PlayerController(self.player), K_SPACE)
    
    def quit(self):
        self._done = True
    
    def run(self):
        self._done = False
        while not self._done:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.quit()
                else:
                    self.input.handle_event(event)
                        
        #update
            
        #draw
        self.screen.fill((0,0,0))
        pygame.display.flip()
        
if __name__ == "__main__":
    game = Game()
    game.run()