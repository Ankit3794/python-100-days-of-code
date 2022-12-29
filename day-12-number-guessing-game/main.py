import random

game_stages = {
    'easy': 10,
    'medium': 7,
    'hard': 5
}

# Get the difficulty of game from user and set attempts
stage = input("Choose difficulty level from 'easy', 'medium' and 'hard': ")
attempts = game_stages.get(stage)
print(f"Total attempts for {stage} difficulty is {attempts}")


def check_answer(user_guess:int, number_to_guess: int, attempts: int):
    """
    Compared user_guess and randomly selected number and return attempts left.
    If wrong guess attempt would be reduced by 1
    """
    if user_guess < number_to_guess:
        print('Too low')
        print(f'{attempts} attempts pending')
        return attempts-1
    elif user_guess > number_to_guess:
        print('Too high')
        print(f'{attempts} attempts pending')
        return attempts-1
    else:
        print('You got it right')
        return attempts


# Select random number and let user guess it
number_to_guess = random.randint(1,100)

user_guess = 0
while attempts > 0 and user_guess != number_to_guess:
    user_guess = int(input('Guess the number: '))
    attempts = check_answer(user_guess, number_to_guess, attempts)
