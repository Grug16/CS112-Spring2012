# Shapes
# =========================================================
# 
# Define a shape object.  This object has abstract (empty) 
# methods for calculating the area and perimeter of the 
# shape.
#
# After that, create classes for Rectangles, Squares, 
# and Circles.
# 
# When done, the code should work like this.
#     >>> r = Rect(3,4)
#     >>> print r.area()
#     12
#     >>> sq = Square(5)
#     >>> print sq.perimeter()
#     20
#     >>> print isinstance(sq, Rectangle)
#     True
#     >>> c = Circle(3)
#     >>> print c.area()
#     28.274333882308138
#
import math
class Shape(object):
    def area (self):
        pass
    def perimeter(self):
        pass

class Rect(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2*(self.width+self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.r = radius
    def area(self):
        return math.pi * self.r**2
    def perimeter(self):
        return 2*math.pi*self.r

class Square(Rect):
    def __init__(self, side):
        self.width = side
        self.height = side
    

        
# Advanced Section
# ---------------------------------------------------------
# Add one more shape type: a polygon.  Polygons are created
# from a list of at least 3 points.
#
# >>> Polygon((0,0), (3,4), (0,4))
# >>> Polygon((0,0), (2,0), (2,2), (0,2))

def distance (a, b):
    return math.sqrt((b[0]-a[0])**2 + (b[1]-a[1])**2)
def triPer (a, b, c):
# Triangle Perimeter
    return  distance(a, b) + distance(b,c) + distance(c,a)
class Polygon(Shape):
    def __init__(self,*points):
        self.pts = points
    def perimeter(self):
        total = 0.0
        for x in range(len(self.pts)):
            a = self.pts[x]
            b = self.pts[x-1]
            total += distance(self.pts[x], self.pts[x-1])
        return total
    def area (self):
        total = 0.0
        for x in range (1, len(self.pts)):
            total +=(self.pts[x][0]*self.pts[x-1][1] - self.pts[x][1]*self.pts[x-1][0])
        return abs(total)/2
            
        
        
            

# Perimeter should be easy to calculate, for area, use 
# method 1 on this site for finding the area of an irregular 
# polygon:
#   http://www.mathopenref.com/polygonirregulararea.html
# 
# You can find the area of a triangle with Heron's formula:
#   http://www.mathopenref.com/heronsformula.html
