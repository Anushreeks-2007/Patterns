import turtle
import colorsys

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Mesmerizing Rainbow Mandala")

pen = turtle.Turtle()
pen.speed(0)
pen.width(2)
pen.hideturtle()

colors = 120

for i in range(colors):
    color = colorsys.hsv_to_rgb(i / colors, 1, 1)
    pen.pencolor(color)

    for j in range(6):
        pen.circle(100 + i, 60)
        pen.left(60)

    pen.left(10)

turtle.done()
