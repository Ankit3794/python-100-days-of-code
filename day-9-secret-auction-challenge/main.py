import os
import art

print(art.logo)
print('Welcome to the secret auction program.')

bids = []

should_end = False

def get_bid_winner():
    max_bid = sorted(bids, key=lambda b: b.get('bid_value'))[-1]
    return f"The winner is {max_bid.get('name')} with a bid of ${max_bid.get('bid_value')}"
    

def clear():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')

while not should_end:
    name = input('What is your name?\n')
    bid_value = int(input('What is your bid? $'))
    bids.append({"name": name, "bid_value": bid_value})

    restart = input("Are there any other biders? Type 'yes' or 'no'\n")
    clear()
    if restart == 'no':
        should_end = True
        print(get_bid_winner())