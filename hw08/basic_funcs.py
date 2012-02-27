#!/usr/bin/env python

# Create a greeter
#    create a greeter that says hello to someone in all lower case.  Use print statements
#
#  ex:
#   >>> greeter("paul")
#   hello, paul
#   >>> greeter(3)
#   hello, 3
#   >>> greeter("WORLD")
#   hello, world

def greeter(name):
    name = str(name)
    name = name.lower()
    print "hello,", name



# Draw a box
#    given a width and a height, draw a box in the terminal.  Use print statements
#
#  ex:
#    >>> box("apples", -3)
#    Error: Invalid Dimensions
#    >>> box(1,1)
#    +
#    >>> box(4,2)
#    +--+
#    +--+
#    >>> box(3,3)
#    +-+
#    | |
#    +-+

def box(w,h):
    if type(w) != int or type(h) != int:
        print "Error: Invalid Dimensions"
        return
    if w <= 0 or h <= 0:
        print "Error: Invalid Dimensions"
        return
    if w == 1:
        top = "+"
    else:
        top = "+" + "-"*(w-2) + "+"
    
    if w == 1:
        side = "|"
    else:
        side = "|" + " "*(w-2) + "|"
    for x in range(h):
        if x == 0:
            print top
        elif x == h-1:
            print top
        else:
            print side




# ADVANCED
# Draw a Festive Tree
#    draw a festive tree based on the specifications.  You will need to discover the arguments 
#    and behavior by running the unittests to see where it fails.  Return a string, do not print.
#
#  ex:
#    >>> print tree()
#        *
#        ^
#       ^-^
#      ^-^-^
#     ^-^-^-^
#    ^-^-^-^-^
#       | |
#       | |

def tree(height=5, length=2, ornament = '-', leaf = '^', star='*'):
    # height, trunk, star, leaf, ornament

    if ornament is None:
         ornament = ' '
    if leaf is None:
        leaf = ' '
    if height <= 3:
        trunk = "|"
    else:
        trunk = "| |"
    
    tr = []
    if star is not None:
        tr.append((height-1)*" "+star)
    for layer in range(1, height+1):
        tr.append(" "*(height - layer) + leaf + (ornament + leaf) * (layer - 1))
    
    if height <=3:
        for x in range((length)):
            tr.append((height-1)*" "+trunk)
           

    else:
        for x in range(length):
            tr.append((height-2)*" "+trunk)
     
    return "\n".join(tr)