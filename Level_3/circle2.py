import turtle
import colorsys

screen = turtle.Screen()
screen.bgcolor("pink")

t = turtle.Turtle()
t.speed(0)
t.width(2)
t.hideturtle()

h = 0
for i in range(200):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    t.pencolor(c)
    t.forward(i * 1.5)
    t.left(91)
    h += 0.005

turtle.done()