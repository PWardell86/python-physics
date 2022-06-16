from pyglet import *
from Point import Point
from Stick import Stick
from random import shuffle, random


movingPoint = None
w = window.Window(500, 500)
batch = graphics.Batch()

x = 100
y = 480
l = 10
space = 15
points = []
sticks = []
segments = 15
holds = 15
for i2 in range(holds):
    points += [Point(x + (i2 * space), y, 2, batch = batch, fixed = True)]
    for i in range(1, segments):
        points += [Point(x + (i2 * space), y - (i * l), 2, batch = batch)]
        sticks += [Stick(points[i + segments * i2 -1], points[i + segments * i2], batch)]

for i in range(0, len(points) - segments, 2):
    sticks += [Stick(points[i], points[i + segments], batch)]

def update(t):
    g = 200
    shuffle(points)
    for s in sticks:
        s.update()

    for p in points:
        p.update(g, t)


@w.event
def on_draw():
    w.clear()
    batch.draw()

@w.event
def on_mouse_press(x, y, b, m):
    global movingPoint
    if b == 4:
        try:
            movingPoint[1].fixed = not(movingPoint[0].fixed)
        except:
            pass
    for p in points:
        dx = p.x - x
        dy = p.y - y
        if abs(dx) <= p.radius * 1.5 and abs(dy) <= p.radius * 1.5:
            movingPoint = [p, p.fixed]
            movingPoint[0].fixed = True
            break

@w.event
def on_mouse_release(x, y, b, m):
    global movingPoint
    try:
        movingPoint[0].fixed = movingPoint[1]
    except TypeError:
        pass
    movingPoint = None

@w.event
def on_mouse_drag(x, y, mx, my, b, m):
    global movingPoint
    try:
        movingPoint[0].x = x
        movingPoint[0].y = y
        movingPoint[0].previousPos = (x, y)
    except TypeError:
        pass
clock.schedule(update)
app.run()