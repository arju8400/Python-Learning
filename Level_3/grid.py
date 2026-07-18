import turtle, random, colorsys
t = turtle.Turtle(); t.speed(0); t.hideturtle(); t.penup()
turtle.bgcolor("black")
for i in range(100):
    h = random.random()
    t.color(colorsys.hsv_to_rgb(h, 1, 1))
    t.goto(random.randint(-100,100), random.randint(-100,100))
    t.dot(random.randint(2,8))
turtle.done()