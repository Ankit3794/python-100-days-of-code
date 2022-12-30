from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()

timmy.shape('turtle')

# draw multiple shapes

def change_color():
    R = random.random()
    B = random.random()
    G = random.random()
    timmy.color(R, G, B)


def draw_shape(num_of_sides):
    angle = 360 / num_of_sides
    for _ in range(num_of_sides + 1):
        timmy.forward(100)
        timmy.right(angle)


for sides in range(3, 11):
    draw_shape(sides)
    change_color()
