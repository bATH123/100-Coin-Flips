"""
Flips 100 coins, heads or tails, and gives a percentage of coins that are heads or tails.
"""


import random


def main():
    coin_heads = 0
    coin_tails = 0
    coin = ['heads', 'tails']
    for x in range(100):
        coin_flip = random.choice(coin)
        if coin_flip == 'heads':
            coin_heads += 1
        else:
            coin_tails += 1
    print(f'The coin landed on heads {coin_heads} times.')
    print(f'The coin landed on tails {coin_tails} times.')


main()