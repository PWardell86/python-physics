from pyglet import shapes
from math import sqrt, sin, cos, atan2
class Stick(shapes.Line):
    def __init__(self, p1, p2, batch):
        super(Stick, self).__init__(p1.x, p1.y, p2.x, p2.y, batch = batch)
        self.lengthSquared = ((p2.x - p1.x) ** 2) + ((p2.y - p1.y) ** 2)
        self.p1 = p1
        self.p2 = p2

    def update(self):
        self.position = (self.p1.x, self.p1.y, self.p2.x, self.p2.y)
        self.resize()

        if not(self.p1.fixed):
            self.p1.position = (self.x, self.y)
        if not(self.p2.fixed):
            self.p2.position = (self.x2, self.y2)
        
    def resize(self):
        dx = self.x2 - self.x
        dy = self.y2 - self.y
        thisLengthsq = dx*dx + dy*dy
        dt = sqrt(thisLengthsq) - sqrt(self.lengthSquared)

        if abs(dt) > 0:
            theta = atan2(dy, dx)
            movex = dt * cos(theta)
            movey = dt * sin(theta)
            div = 2

            if not(self.p1.fixed or self.p2.fixed):
                self.x2 -= (movex) / div
                self.y2 -= (movey) / div
                self.x += movex / div
                self.y += movey / div
            elif not(self.p2.fixed):
                self.x2 -= (movex)
                self.y2 -= (movey)
            elif not(self.p1.fixed):
                self.x += movex
                self.y += movey