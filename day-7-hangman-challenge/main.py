import random
import hangman_art as art

game_words = ['practice', 'hangman', 'challenge']

chosen_word = game_words[random.randint(0, len(game_words)-1)]

guess_word = [i for i in '_' * len(chosen_word)]

print(art.logo)
print('Guess the word')
print(guess_word)

total_lives = 7

def add_to_guess_word(char):
    for i, wc in enumerate(chosen_word):
        if wc == char:
            guess_word[i] = char

while total_lives > 0:
    if chosen_word == "".join(guess_word):
        print("You win!!!")
        break

    char_guess = input('Guess the word\n')
    if char_guess in chosen_word:
        add_to_guess_word(char_guess)
        print(" ".join(guess_word))
    else:
        total_lives -= 1
        if total_lives == 0:
            print('You lose!!!')
            break
        else:
            print(art.stages[total_lives])