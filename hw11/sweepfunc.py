import time
from random import randrange
print "Welcome to MineSweeper!"
width = int(raw_input("Choose Board Width: "))
height = int(raw_input("Choose Board Height: "))
bombs = int(raw_input("Number of Mines: "))

board = []
flags = []
def construct (xdimension=10, ydimension=10, numbombs=10):
    if xdimension < 1:
        xdimension = 1
    if ydimension < 1:
        ydimension = 1
    del board[:]
    del flags[:]
    for y in range(ydimension):
        board.append([])
        for x in range(xdimension):
            board[y].append('-')
    
    #build flag table
    for y in range(ydimension):
        flags.append([])
        for x in range(xdimension):
            flags[y].append('-')
            
    
    c=0
    if numbombs >= xdimension * ydimension:
        numbombs = xdimension * ydimension - 1
    while c < numbombs:
        x = randrange(xdimension)
        y = randrange(ydimension)
        if not board[y][x]=='B':
            board[y][x]= 'B'
            c += 1
    
    for y in range (ydimension):
        print board[y]


def choice (y, x):
    if x < 0 or x >= len(board[0]):
        print "X out of bounds"
        return
    if y < 0 or y >= len(board):
        print "Y out of bounds"
        return
    if board[y][x] == '-':
        bombcount = 0
        for i in range (-1,2):
            for j in range (-1,2):
                if i or j: #making sure they are both not 0
                    if safecheck(i+y,j+x)=='B':
                        bombcount += 1
        board[y][x] =  str(bombcount)
        #check all adjacent
        if board[y][x]== '0':
            checkaround(y,x)
    else:
        if board[y][x] == 'B':
            return 'Bomb'
       # else:
            #print "Already Chocsen: ",board[y][x]
    #showboard()

def checkaround(y,x):
    for i in range (-1,2):
        for j in range (-1,2):
            if i or j:
                choice(i+y,j+x)

def safecheck(y, x):
    if x < 0 or x >= len(board[0]):
        print "X out of bounds"
        return
    if y < 0 or y >= len(board):
        print "Y out of bounds"
        return
    return board[y][x]


def showboard():
    for y in range (len(board)):
        print board[y]

def checkwin():
    dashcount = 0
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == '-':
                dashcount +=1
    if dashcount == 0:
        return True
    else:
        return False
    

def printboard(line = -1):
    userboard = board
    dashcount = 0
    for y in range(len(board)):
        for x in range(len(board[0])):
            if userboard[y][x] == 'B':
                userboard[y][x] = '-'
    for y in range (len(board)):
        if y == line:
            print "->",userboard[y]
        else:
            print "  ",userboard[y]


playing = True
while playing == True:
    printboard()
    
    
    
print "Thank you for playing"
    
    
    
    