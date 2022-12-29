import random
from game_data import data
import os
import art


def clear():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')


score = 0
game_over = False

while not game_over:
    print(art.logo)
    if score > 0:
        print(f"You are right! Current score: {score}.")
    
    option_a = random.choice(data)
    option_b = random.choice(data)

    while option_b == option_a:
        option_b = random.choice(data)

    correct_answer = 'A' if option_a.get('follower_count') > option_b.get('follower_count') else 'B'

    print(f"""
Compare A: {option_a.get('name')}, a {option_a.get('description')}, from {option_a.get('country')}
    {art.vs}
Against B: {option_b.get('name')}, a {option_b.get('description')}, from {option_b.get('country')}
    """)

    print(f"Correct answer - {correct_answer}")

    guess = input("Who has more follower? Type 'A' or 'B': ")
    if guess.upper() == correct_answer:
        score += 1
        clear()
    else:
        clear()
        print(art.logo)
        print(f"Sorry, that's wrong. Final Score {score}")
        break