import turtle
import colorsys
screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
t.width(2)
t.hideturtle()
h = 0
for i in range(360):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    t.pencolor(c)
    t.circle(i *0.3)
    t.forward(i *0.4)
    t.left(18)
    h += 0.003

turtle.done()
