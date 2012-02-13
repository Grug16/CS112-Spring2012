#!/usr/bin/env python
"""tictactoe.py

A Simple tic tac toe game
"""

# Implement a version of tic tac toe

# player X = 1.  Player O = 0

# Note to TA: The "move" function for some reason does not recognize
# the "player" variable outside itself, making it impossible to change player.
# otherwise, fully functional.

player = 1
game = 1


board = [[1, 2, 3],[4,5,6],[7,8,9]]

print"""
    %s|%s|%s
    -----
    %s|%s|%s
    -----
    %s|%s|%s
    """ % (board[0][0], board[0][1], board[0][2], board[1][0], board[1][1], board[1][2], board[2][0], board[2][1], board[2][2],)


def wincheck ():
    for x in range (3):
        if board[x][0] == board [x][1]== board [x][2]:
            print "Victory!"
            game = 0
    for x in range (3):
        if board[0][x] == board [1][x]== board [2][x]:
            print "Victory!"
            game = 0
    
    if board[0][0] == board [1][1]== board [2][2]:
        print "Victory!"
        game = 0
    if board[2][0] == board [1][1]== board [2][0]:
        print "Victory!"
        game = 0
player = 1
def move(space, player):
    for y in range(3):
        for x in range(3):
            if board[y][x] == space:
                if player == 1:
                    board[y][x] = "X"
                    player = 0
                else:
                    board[y][x] = "O"
                    player = 1

while game == 1:
   
        
    move(int(raw_input("Player %i's turn.  Pick a space to play: " %(player))), player)
    print"""
    %s|%s|%s
    -----
    %s|%s|%s
    -----
    %s|%s|%s
    """ % (board[0][0], board[0][1], board[0][2], board[1][0], board[1][1], board[1][2], board[2][0], board[2][1], board[2][2],)

    wincheck()
    
