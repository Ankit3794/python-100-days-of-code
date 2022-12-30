import turtle as t

timmy = t.Turtle()
screen = t.Screen()


def move_forward():
    timmy.forward(15)

def move_backward():
    timmy.backward(15)

def turn_left():
    timmy.setheading(timmy.heading() + 10)

def turn_right():
    timmy.setheading(timmy.heading() - 10)


def clear():
    timmy.reset()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")
screen.exitonclick()
