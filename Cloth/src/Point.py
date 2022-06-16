from pyglet import shapes

class Point(shapes.Circle):
    def __init__(self, x, y, radius, batch, fixed = False):
        super(Point, self).__init__(x, y, radius, batch = batch)
        self.previousPos = [self.x, self.y]
        self.fixed = fixed
        self.radius = radius
        
    def update(self, g, t):
        if not(self.fixed):
            px = self.x
            py = self.y
            mx = (self.x - self.previousPos[0]) * .99
            my = (self.y - (self.previousPos[1])) * 0.98
            my -= g*t*t

            self.x += mx
            self.y += my

            self.previousPos = [px, py]