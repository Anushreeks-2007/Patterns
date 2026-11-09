import turtle
import colorsys
import math

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(800, 800)
screen.title("Hypnotic Moving Pattern")
screen.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.width(2)

angle = 0
hue = 0

def animate():
    global angle, hue

    pen.clear()

    for i in range(36):
        color = colorsys.hsv_to_rgb((hue + i / 36) % 1, 1, 1)
        pen.pencolor(color)

        pen.penup()
        pen.goto(0, 0)
        pen.setheading(angle + i * 10)
        pen.forward(40 + 150 * math.sin(math.radians(angle * 2 + i * 10)))
        pen.pendown()

        pen.circle(35 + 15 * math.sin(math.radians(angle + i * 10)))

    angle += 2
    hue = (hue + 0.005) % 1

    screen.update()
    screen.ontimer(animate, 20)

animate()
turtle.done()