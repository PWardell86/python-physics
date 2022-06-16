from plistlib import InvalidFileException
from PhysicsExceptions import *
from math import sqrt, atan2
class Vector2D(tuple):
    def __init__(self, x, y):
        super(Vector2D, self).__init__((x, y))
        self.calculateMagnitude()

    def __add__(self, v2):
        inputType = type(v2)
        if inputType != Vector2D:
            raise InvalidArgumentException(f"Can only add Vector2D and Vector2D, not Vector 2D and {inputType}")
        return (self[0] + v2[0], self[1] + v2[1])
    
    def __mul__(self, scalar):
        inputType = type(scalar)
        if inputType != int:
            raise InvalidArgumentException(f"Can only perform scalar multiplication, not with type {inputType}")
        return (self[0] * scalar, self[1] * scalar)

    def __rmul__(self, scalar):
        return self * scalar

    def getMagnitude(self):
        return sqrt((self[0] ** 2) + (self[1] ** 2))
    
    def getAngle(self):
        return atan2(self[1], self[0])
    
    def getX(self):
        return self[0]

    def getY(self):
        return self[1]