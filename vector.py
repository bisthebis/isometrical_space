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

    def __str__(self):
        return "({}, {}, {})".format(self.x, self.y, self.z)

    def __add__(self, other):
        """ Returns a new vector that is the sum of its args """
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        """ Returns difference of vectors """
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar):
        """ Multiplication by a real number """
        return Vec3(scalar * self.x, scalar * self.y, scalar * self.z)

    def __truediv__(self, scalar):
        """ Division is multiplication by inverse """
        scale = 1.0 / scalar
        return self * scale

    def normalized(self):
        """ Return a new vector with the same direction but of length 1"""
        return self / self.length()

    def normalize(self):
        """ Modifies the vector make its length 1 """
        new_vec = self.normalized()
        self.x = new_vec.x
        self.y = new_vec.y
        self.z = new_vec.z
