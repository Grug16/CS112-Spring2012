#!/usr/bin/env python

import math

# Distance formula
#   calculate a function called "distance" to calculate the distance between two points.
#   http://www.purplemath.com/modules/distform.htm
#   ex: 
#      >>> distance((0,0), (3,4))
#      5

def distance(a, b):
    x1,y1 = a
    x2,y2 = b
    aline = x1 - x2
    bline = y1 - y2
    return math.sqrt(aline**2 + bline**2)

# ADVANCED
# Normalizing Vectors
#   normalize a vector of length N.  If given all zeros, just spit back the same vector
#   http://www.fundza.com/vectors/normalize/index.html

#   ex:
#     >>> normalize((1,1))
#     [0.70710678118654746, 0.70710678118654746]
#     >>> normalize([0,0,0])
#     [0,0,0]
#     >>> normalize([1,1,1,1])
#     [0.25, 0.25, 0.25, 0.25]

def normalize(vector):
    total = 0
    for n,v in enumerate(vector):
        total += vector[n]**2
    distance = math.sqrt(total)
    if not (distance == 0):
        for n,v in enumerate(vec):
            vector[n] = vector[n] / distance
        
    return vector
