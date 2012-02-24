#!/usr/bin/env python

import string
###################### 
#  Helper Functions
######################

def splitparts(s):
    "splitparts takes a string and returns all chunks.  Chunks are any space separated or comma separated values"
    return s.replace(",", " ").split()
    
def a2idx(c):
    "converts a letter to it's index value"
    
    return string.ascii_uppercase.find(c.upper())
    
    

def idx2a(i):
    return string.ascii_uppercase[i]

##############################################
# Object Functions
#    functions relating to moves and stones
###############################################

def parse_stones(s):
    """given a list of nums (chunks) return a list of stone piles.  Piles cannot be less than 0
    and can be a maximum of 99 stones

    >>> parse_stones("12, 13")
    [12, 13]
    >>> parse_stones("0 200 4 5")
    [99, 4, 5]
    """
    s = [int(p) for p in splitparts(s)]
    return [min(v,99) for v in s if v > 0]

# moves are [pile, amount] => [int, int]

def parse_move(s):
    """given an attempted move, parse the input into a "move list"

    >>> parse_move("A  3")
    [0, 3]
    >>> parse_move("this isn't valid")
    None
    """
    s = splitparts(s)
    if len(s) != 2:
        return None
    if s[0].isalpha():
        s[0] = a2idx(s[0])
    else:
        return 0
    if s[1].isdigit():
        s[1]=int(s[1])
    else:
        return None
    return s[0],s[1]

def valid_move(mv, piles):
    """check if a given move can actually be completed

    >>> valid_move(None, [3,3])
    False
    >>> valid_move([0,3], [3,3])
    True
    >>> valid_move([1,20], [3,3])
    False
    >>> valid_move([20,2], [3,3])
    False
    """
    if mv == None:
        return False
    if mv[0] >= len(piles):
        return False
    if mv[1] > piles[mv[0]] or mv[1] < 1:
        return False
    return True


def move(mv, piles):
    "perform a move"
    piles[mv[0]] -= mv[1]

#####################################
#  Output Functions
#     functions which format strings
#####################################
def header(piles):
    "draw the header of the game table"
    piles = [idx2a(i) for i in range(len(piles))]
    l = " "
    l += "  ".join(piles)
    l += " | Move"
    return l

def prompt(piles, player):
    "format the input prompt"
    p = ""
    p += " ".join("%2d" % i for i in piles)
    p += " | "
    p += "Player %d:  " %(player+1)
    return p


# do not touch, already done
def separater(piles):
    "creates a separater under the header, long enough to cover all the piles"
    total = 21 + len(piles)
    total += (len(piles) - 1) * 2
    return "=" * total

###########################################
#  MAIN -- DO NOT TOUCH BELOW THIS POINT 
###########################################
def main():
    piles = parse_stones(raw_input("Number of stones in each pile:  "))
    print ""

    print header(piles)
    print separater(piles)

    # init 
    player = 0      # player will be 0 or 1

    # loop as long as any value in piles != 0
    while any(piles): 
        inp = parse_move( raw_input(prompt(piles, player)) )

        # check for valid input
        if not valid_move(inp, piles):
            print "*Error*  Invalid Move"
            continue

        move(inp, piles)
        player = (player + 1) % 2

    # declare winner
    print "Player %d wins!!!" % (player + 1)

if __name__ == "__main__":
    main()
