import turtle, colorsys
t = turtle.Turtle(); t.speed(0); t.hideturtle()
turtle.bgcolor("black")
h = 0
for i in range(100):
    t.pencolor(colorsys.hsv_to_rgb(h, 1, 1))
    t.circle(100)
    t.left(3.6)
    h += 0.01
turtle.done()