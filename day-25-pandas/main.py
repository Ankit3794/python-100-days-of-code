import turtle
import pandas as pd

state_data = pd.read_csv("50_states.csv")
all_states = state_data["state"].to_list()

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

guessed_states = []

while len(guessed_states) < len(all_states):
    answer_state = turtle.textinput(title=f"{len(guessed_states)}/50 States correct",
                                    prompt="What's another state name?").title()

    if answer_state == "Exit":
        states_to_learn = [s for s in all_states if s not in guessed_states]
        with open("states_to_learn.csv", "w") as file:
            file.write("\n".join(states_to_learn))
        break

    if answer_state in all_states:
        state_row = state_data[state_data["state"] == answer_state.title()]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(state_row.x.item(), state_row.y.item())
        t.write(answer_state.title())
        guessed_states.append(answer_state)
    else:
        print("This is not correct state")
