import turtle, colorsys
t = turtle.Turtle(); t.speed(0); t.hideturtle()
turtle.bgcolor("black")
h = 0
for i in range(150):
    t.pencolor(colorsys.hsv_to_rgb(h, 1, 1))
    t.forward(150)
    t.backward(150)
    t.right(61)
    h += 0.006
turtle.done()