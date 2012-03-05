from random import randrange
import pygame
from pygame.locals import *
FPS = 30
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
        flags[y][x] = 'C'
        bombcount = 0
        for i in range (-1,2):
            for j in range (-1,2):
                if i or j: #making sure they are both not 0
                    if safecheck(i+y,j+x)=='B':
                        bombcount += 1
        board[y][x] =  bombcount
        #check all adjacent
        if board[y][x]== 0:
            checkaround(y,x)
    else:
        if board[y][x] == 'B':
            return "Bomb"
        else:
            print "Already Chocsen: ",board[y][x]

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

def draw_flag(x,y):
    pole = pygame.Rect((x+10,y+5), (5,30))
    flag = pygame.Rect((x+10,y+5), (20,10))
    pygame.draw.rect(screen, (200,0,0), flag)
    pygame.draw.rect(screen, (0,255,255), pole)
    
def reset_button(x,y):
    button = pygame.Rect((x,y), (tile*2, tile))
    pygame.draw.rect(screen, (100,0,0), button)
    resetword = font.render("Reset", True, (200,200,200),(100,0,0))
    screen.blit(resetword,(x+2,y+5))

def time_display(x,y, time):
    timecount = font.render(str(time/30), True, (200,200,200),(0,0,0))
    screen.blit(timecount,(x+5,y+5))

def flagcount_display(x,y, bombs):
    flagcount = smallfont.render(str(remainingflags(bombs)), True, (100,255,100),(0,0,0))
    screen.blit(flagcount,(x+5,y+5))

def remainingflags(bomb_quantity):
    flagcount = bomb_quantity
    for y in range(len(flags)):
        for x in flags[y]:
            if x == 'F':
                flagcount-=1
    
    return flagcount
            


def checkwin():
    dashcount = 0
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == '-':
                dashcount +=1
    if dashcount == 0:
        print "Win"
        return True
    else:
        return False

tile = 40
C_BORDER = 0,0,0
C_HIDDEN = 80,80,80
C_ACTIVE = 255,255,255
C_CLEARED = 180,180,180
C_BOMB = 255,0,0
C_FLAG = 0,0,255
C_LETTER = 255,255,255
pygame.font.init()
font = pygame.font.Font(None, 40)
smallfont = pygame.font.Font(None, 40)
def clear_square(world,x,y):
    choice(y, x)

width = int(raw_input("Board Width: "))
height = int(raw_input("Board Height: "))
bombs = int(raw_input("Number of Bombs?: "))

construct(width, height, bombs)
gameover = False
screen = pygame.display.set_mode((width*tile, height*tile + tile))
def game():
    
    time = 0
    lmb_clicked = False
    rmb_clicked = False
    action_clear_square = False
    action_flag_square = False
# loop
    clock = pygame.time.Clock()
    done = False
    gameover = False
    while not done:
        # input
        for event in pygame.event.get():
            if event.type == QUIT:
                done = True
                print "Quit"
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                print "Escaped"
                done = True


            # mouse
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                lmb_clicked = True
            elif event.type == MOUSEBUTTONUP and event.button == 1:
                lmb_clicked = False
                action_clear_square = True
            elif event.type == MOUSEBUTTONDOWN and event.button == 3:
                rmb_clicked = True
                print "Right click"
            elif event.type == MOUSEBUTTONUP and event.button == 3:
                rmb_clicked = False
                action_flag_square = True

        # update
        if action_flag_square:
            x,y = pygame.mouse.get_pos()
            x /= tile
            y /= tile
            if y*tile <= (height * tile - tile):
                if flags[y][x] == 'F':
                    flags[y][x] = '-'
                    print "Unflagged"
                elif flags[y][x] == '-':
                    flags[y][x] = 'F'
                    
                    print "Flagged"
            action_flag_square = False
            
            
        if action_clear_square:
            #
            x,y = pygame.mouse.get_pos()
            x /= tile
            y /= tile
            if y*tile <= (height * tile - tile):
                if choice(y, x) == 'Bomb': #choice performs the selection process, and returns if a bomb is chosen
                    gameover = True
                flags[y][x] = 'C' #c for cleared.  It will not toggle
            
            action_clear_square = False

        # display
        screen.fill(C_BORDER)
        
        # draw each cell
        
        #RESET  BUTTON
        reset_button(0, height*tile)
        if lmb_clicked and pygame.Rect((0,height*tile), (tile*2, tile)).collidepoint(pygame.mouse.get_pos()): #reset button
            print "resetting"
            construct(width, height, bombs)
            time = 0
        #timer
        time_display(tile*2, height*tile, time)
        
        flagcount_display(tile*3, height*tile, bombs)
            
            
        for x in range(len(board[0])):
            for y in range(len(board)):
                # get rect for cell
                rect = pygame.Rect(x*tile, y*tile, tile, tile)
                
                # color for cell
                if board[y][x]!= '-' and board[y][x] != 'B':
                    bg_color = C_CLEARED
                elif lmb_clicked and rect.collidepoint(pygame.mouse.get_pos()): #lmb_clicked and 
                    bg_color = C_ACTIVE
                elif rmb_clicked and rect.collidepoint(pygame.mouse.get_pos()): #lmb_clicked and 
                    bg_color = C_FLAG
                
                    
                else:
                    bg_color = C_HIDDEN

                # draw background
                screen.fill(bg_color, rect.inflate(-2, -2))

                # draw cleared graphics
                if board[y][x] == '-' or board[y][x] == 'B':
                    if flags[y][x] == 'F':
                        draw_flag(x*tile,y*tile)
                if board[y][x] == 'B' and gameover == True:
                    pygame.draw.ellipse(screen, C_BOMB, rect.inflate(-tile/2, -tile/2))
                
                #numbers.  Number color changes based on value
                if board[y][x] != '-' and board[y][x] != 'B' and board[y][x]!='0':
                    text = font.render(str(board[y][x]), True, (30*int(board[y][x]), 255/(int(board[y][x] + 1)),0),C_CLEARED)
                    loc = text.get_rect()
                    loc.center = rect.center
                    screen.blit(text,loc)  #(x*tile + 4, y*tile + 4))
                    
                
                
                
        # refresh
        if checkwin():
            gameover = True
        pygame.display.flip()
        clock.tick(FPS)
        time += 1
        
def main():
    pygame.init()
    game()
    
main()