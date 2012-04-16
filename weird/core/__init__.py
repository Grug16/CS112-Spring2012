#!/usr/bin/env python

import pygame

from core.input import InputManager


class Game(object):
    size = 800,600
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        
        self.input = InputManager()
    
    def quit(self):
        self._done = True
    
    def run(self):
        self.done = False
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