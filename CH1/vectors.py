'''
Euclidean Vectors

This script will show two dimensional vectors 
'''

import math
from math import hypot

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        #This method is called by the repr built-in to get
        #the string representation of the object for inspection.
        #If we didn't implement __repr__, vector instance would simply
        #call the Vector object.
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
