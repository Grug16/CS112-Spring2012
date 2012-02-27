#!/usr/bin/env python

import math
from random import randrange

def distance(a,b):
    x1,y1 = a
    x2, y2 = b
    return math.sqrt((x2-x1)**2 + (y2-y1) ** 2)

def randtuple(n, lo, hi):
    "returns a random n-tuple"
    return tuple(randrange(lo,hi) for i in range (n))

def randtuple2(*hi): # the asterisk * means it can be any variable amount...?
    "returns a random n-tuple"
    return tuple(randrange(i) for i in hi)
    
def randtuple3(*bounds): # the asterisk * means it can be any variable amount...?
    "returns a random n-tuple"
    bounds = list(bounds)
    for i,bound in enumerate(bounds):
        if type(bound) == int:
            bounds[i]=[bound]
    return tuple(randrange(*arg) for arg in bounds)