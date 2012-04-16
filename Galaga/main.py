#!/usr/bin/env python
import pygame
from pygame.locals import *
from pygame.sprite import Group, GroupSingle, groupcollide

from player import Player
from enemy import Enemy, FastEnemy
from random import randrange

SCREEN_SIZE = 480,640
BG_COLOR = 30,0,100

def main():
    #initialize pygame
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    bounds = screen.get_rect()
    spawntime = 60
    spawnticker = 0
    fast_spawn_counter = 0
    score = 0
    #initialize the game
    player = Player(bounds.center, bounds) #creates a new player object, passes variables to it.
    player_grp = GroupSingle(player)
    enemies = Group() #emtpy sprite group
    
    font = pygame.font.Font(None, 40)
    #game loop
    done = False
    clock = pygame.time.Clock()
    while not done: 
        #input
        for event in pygame.event.get():
            if event.type == QUIT:
                done = True
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                done = True
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                player.shoot()
            elif event.type == KEYDOWN and event.key == K_SPACE and not player.alive():
                player = Player(bounds.center, bounds) # respawns player
                player_grp.add(player)
                score = 0
                for enemy in enemies:
                    enemy.kill()
                # can also do   enemies.empty()
            
                
        
        
        #update
        player_grp.update() #only if the player is in the player_grp sprite group.  See destroyed area
        player.bullets.update() #update everything in the Bullets list
        enemies.update()
        
        
        #collisions
        groupcollide(player_grp, enemies, True, False) #first group, second group, then which gets killed
        
        for enemy in groupcollide(enemies, player.bullets, True, True):
            if player.alive():
                score +=1 #counts how many are intersecting
        
        #spawn
        spawnticker += 1
        if spawnticker >= spawntime:
            #print "spawned!"
            enemies.add(Enemy((randrange(0,400),randrange(0,200)),bounds))
            spawnticker = 0
        fast_spawn_counter += 1
        if fast_spawn_counter >= 45:
            #print "spawned!"
            x = randrange (0, 480)
            enemy = FastEnemy((x,0), bounds)
            enemies.add(enemy)
            fast_spawn_counter = 0
        
        
        
        #draw
        
        screen.fill(BG_COLOR) # fill then draw
        player.bullets.draw(screen) #bullets is the list of all bullets
        player_grp.draw(screen)
        enemies.draw(screen)
        score_text = font.render("Score: %08d" %score, False, (255,255,255))
        screen.blit(score_text, (5,5))
        pygame.display.flip()
        clock.tick(30)
# when this program is run, call "main()".  Makes sure that it will only run if
# chosen to run, as opposed to being called by another program.
if __name__ == "__main__":
    main()