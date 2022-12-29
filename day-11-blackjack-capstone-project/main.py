import random
import art
import os

def get_random_card():
    """
    Get random cards.
    """
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    return random.choice(cards)


def is_black_jack(cards:list):
    return len(cards) == 2 and sum(cards) == 21


def get_normalized_score(cards:list):
    """
    Returns total score of cards.
    If Ace and 10 value cards are there and len(cards) > 2 then Ace value is calculated as 1.
    """
    if 11 in cards and 10 in cards and len(cards)>2:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def check_for_game_over(player_cards, computer_cards):
    player_score = get_normalized_score(player_cards)
    computer_score = get_normalized_score(computer_cards)

    game_over_result = ''
    if player_score > 21:
        game_over_result = 'You went over... Computer wins 🙃'
    elif computer_score > 21:
        game_over_result = 'Computer went over... You win 😀'
    elif is_black_jack(player_cards) and is_black_jack(computer_cards):
        game_over_result = 'Both got blackjack... Draw!!!'
    elif is_black_jack(player_cards):
        game_over_result = 'You wins 😀'
    elif is_black_jack(computer_cards):
        game_over_result = 'Computer wins 🙃'

    if game_over_result:
        print(f"Your cards: {player_cards}")
        print(f"Computer's cards: {computer_cards}")
        print(game_over_result)
        quit()


def declare_result(player_cards, computer_cards):
    """
    Compares player_cards and computer_cards.
    If anyone's total is above 21 then opponenent wins
    else, highest scorer wins!
    """
    player_score = get_normalized_score(player_cards)
    computer_score = get_normalized_score(computer_cards)

    if player_score > computer_score:
        return 'You wins 😀'
    else:
        return 'Computer wins 🙃'


def clear():
    """
    Clears the terminal.
    """
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')


print(art.logo)

player_cards = []
computer_cards = []

for _ in range(2):
    player_cards.append(get_random_card())
    computer_cards.append(get_random_card())

print(f"Your cards: {player_cards}")
print(f"Computer's first card: {computer_cards[0]}")

check_for_game_over(player_cards, computer_cards)

choice = input("Type 'y' to choose another card or 'n' to pass: ")
if choice == 'y':
    player_cards.append(get_random_card())
    check_for_game_over(player_cards, computer_cards)
else:
    while sum(computer_cards) < 17:
        computer_cards.append(get_random_card())
        check_for_game_over(player_cards, computer_cards)
    
    print(f"Your final hand: {player_cards}")
    print(f"Computer's final hand: {computer_cards}")
    print(declare_result(player_cards=player_cards, computer_cards=computer_cards))





