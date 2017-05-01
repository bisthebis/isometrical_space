import math

class Vec3:
    """ 3D vectorial class, with real coordinates"""
    x = 0.0
    y = 0.0
    z = 0.0

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def length_squared(self):
        """Square of the length. (faster than length because square root isn't needed)"""
        return self.dot(self)

    def length(self):
        """ Length of the vector, aka sqrt of self.dot(self)"""
        return math.sqrt(self.length_squared())

    def dot(self, other):
        """ Dot product. Returns a number """
        return self.x * other.x + self.y * other.y + self.z * other.z

    def __add__(self, other):
        """ Returns a new vector that is the sum of its args """
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        """ Returns difference of vectors """
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)




"""Tests"""
a = Vec3(1,2,3)
print ((a + a + a - a).length())