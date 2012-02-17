#!/usr/bin/env python
"""nims.py

A simple competitive game where players take stones from stone piles.
"""
print "Welcome to Nims.  Whoever takes the last stone loses."

stonecount = int(raw_input("Number of stones in the pile: "))
maxtake = int(raw_input("Max number of stones per turn: "))
player = 1
taken = 0

while stonecount>0:
    # Ask player for stones taken.
    taken = int( raw_input("%i stones left.  Player %i [1-%i]: " % (stonecount, player, maxtake)))
    if taken >= 1 and taken <= maxtake:
        if taken <= stonecount:
            # Successful Move
            stonecount -= taken
            if player == 1: # Switches Players
                player = 2
            else:
                player = 1
        else:
            print "Not enough stones."
    else:
        print "Invalid stone selection"


print "Player %i wins!" % (player)