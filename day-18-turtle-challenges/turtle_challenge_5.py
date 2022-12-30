from turtle import Turtle, Screen
import random

# Spirograph

timmy = Turtle()
screen = Screen()

timmy.shape('turtle')
timmy.pensize(3)
timmy.speed('fastest')

def change_color():
    R = random.random()
    B = random.random()
    G = random.random()
    timmy.color(R, G, B)

def draw_spirograph(size_gap):
    for _ in range(int(360/size_gap)):
        timmy.circle(120)
        change_color()
        timmy.setheading(timmy.heading() + size_gap)

draw_spirograph(10)

screen.exitonclick()

