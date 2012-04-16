import pygame
from pygame.locals import *

class KeydownListener(object):
    def on_keydown(self, event): pass
    def on_keyup(self, event): pass


class MouseListener(object):
    def on_click(self, event): pass
    def on_motion(self,event): pass

class InputManager(object):
    def __init__(self):
        self._key = []
        self._mouse = []
        
    
    def add_listener(self, listener, *keys):
        self._key.append(listener)
    
    def add_mouse_listener(self,listener):
        self._mouse.append(listener)
            
    def handle_event(self,event):
        if event.type == KEYDOWN and event.key in self._listeners:
            for listener in self._listeners[key]:
                listener.on_keydown(event)
            
    
    def handle_event(self, event):
        if event.type == KEYDOWN and event.key == K_SPACE:
            print "Awesome Sauce"
            print "sounds.play('jump')"
        elif event.type == KEYDOWN and event.key == K_RETURN:
            print "With Fries"