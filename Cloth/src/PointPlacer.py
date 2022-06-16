from pyglet import *
dragging = False
w = window.Window(500, 500)
batch = graphics.Batch()


points = ""

myShapes = []

@w.event
def on_draw():
    w.clear()
    batch.draw()

@w.event
def on_mouse_press(x, y, b, m):
    global points, myShapes
    if b == 1: # Left left
        points += ",Point(%d, %d, 2, batch)" % (x, y)

    elif b == 4: #Right click
        points += ",Point(%d, %d, 2, batch, fixed = True)" % (x, y)
    myShapes += [shapes.Circle(x, y, 10, batch = batch)]
app.run()
print(points)