import turtle as t
import random as rd

colors = [(233, 233, 232), (231, 233, 237), (236, 231, 233), (224, 233, 227), (207, 160, 82), (54, 88, 130), (145, 91, 40), (140, 26, 49), (221, 207, 105), (132, 177, 203), (158, 46, 83), (45, 55, 104), (169, 160, 39), (129, 189, 143), (83, 20, 44), (37, 43, 67), (186, 94, 107), (187, 140, 170), (85, 120, 180), (59, 39, 31), (88, 157, 92), (78, 153, 165), (194, 79, 73), (45, 74, 78), (80, 74, 44)]

def get_random_color():
    return rd.choice(colors)

timmy = t.Turtle()
screen = t.Screen()
screen.colormode(255)
timmy.pensize(5)
timmy.speed('fastest')

no_of_dots = 15
gap_between_dots = 15

def draw_line(no_of_dots, gap_between_dots):
    for _ in range(no_of_dots + 1):
        timmy.dot()
        timmy.penup()
        timmy.forward(gap_between_dots)
        timmy.color(get_random_color())
        timmy.pendown()
        timmy.dot()
        timmy.penup()

for _ in range(no_of_dots + 1):
    draw_line(no_of_dots, gap_between_dots)
    timmy.setposition(0, timmy.ycor() + gap_between_dots)

screen.exitonclick()