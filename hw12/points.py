# Point Object
# =====================================
# Create a Point point class.  Point objects, when created, look like this:
#     >>> pt = Point(3,4)
#     >>> print pt.x
#     3
#     >>> print pt.y
#     4
#
# In addition points have the following methods:
#    distance(self, other):
#        calculates the distance between this point and another
#    
#    move(self, x, y):
#        sets the points location to x,y
# 
#    translate(self, x, y):
#        offsets the point by x and y
# 
#    When all done, points should work like this:
#
#    >>> a = Point(0,0)
#    >>> b = Point(0,0)
#    >>> b.move(2, 2)
#    >>> print b.x, b.y
#    2 2
#    >>> b.translate(1,2)
#    >>> print b.x, b.y
#    3 4
#    >>> print a.distance(b)
#    5
#
import math
class Point(object):
    def __init__(self, x,y):
        self.x = x
        self.y = y
    def move(self, i, j):
        self.x = i
        self.y = j
    def translate (self, i, j):
        self.x += i
        self.y += j
    def distance (self, other):
        return math.sqrt((other.x-self.x)**2 + (other.y-self.y)**2)

# Advanced Section:
# ---------------------------------------
# Add the following function:
    def slope(self, other):
        dy = float(other.y - self.y)
        dx = float(other.x - self.x)
        if dx == 0:
            return None
        else:
            return dy / dx
#         calculate the slope between two points
#
    def extrapolate(self, slope, distance):
    # Calculate it from zero, then add to the original point.
        if slope == None:
            return Point(self.x, self.y + distance)
        theta = math.atan(float(slope))
        y = math.sin(theta)
        x = math.cos(theta)
        x *=distance
        y *=distance
        return Point((self.x + x), (self.y + y))
    # Attempt to find the X and Y that give the distance we want    
        return normal * distance
#         returns a point along the line defined by slope
#         a given distance away
#
# Also, add the following special python methods:
    def __eq__(self, other):
        if isinstance(other, Point):
            if other.y == self.y and other.x == self.y:
                return True
            else: return False
        else:
            return False

#         checks if other is a Point and is equal to self
#
    def __str__(self):
        return str("("+str(self.x) + "," + str(self.y)+")")


#         returns a string representation of the point 
#     
#     >>> print Point(3,4)
#     (3,4)
#     >>> a = Point(1,2)
#     >>> b = Point(1,2)
#     >>> print a == b
#     True
