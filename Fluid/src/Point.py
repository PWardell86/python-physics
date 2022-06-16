from pyglet import shapes
from Force import Force
from Vector import Vector2D
from PhysicsExceptions import *

class Point(shapes.Circle):
    def __init__(self, x, y, radius, mass, batch, fixed = False, velocity = Vector2D(0, 0)):
        super(Point, self).__init__(x, y, radius, batch = batch)
        self.previousPos = [self.x, self.y]
        self.velocity = velocity
        self.fixed = fixed
        self.radius = radius
        self.mass = mass
        
    def update(self, g, t):
        if not(self.fixed):
            px = self.x
            py = self.y
            mx = (self.x - self.previousPos[0]) + self.velocity.getXComp()
            my = (self.y - self.previousPos[1]) + self.velocity.getYComp()
            my -= g*t*t

            self.x += mx 
            self.y += my

            self.previousPos = (px, py)

    def addForce(self, force: Force):
        try:
            acceleration = Vector2D(force.getX() / self.mass, force.getY() / self.mass)
        except ZeroDivisionError:
            raise ZeroMassError("Cannot calculate acceleration from 0 mass")
        self.velocity += acceleration


        

