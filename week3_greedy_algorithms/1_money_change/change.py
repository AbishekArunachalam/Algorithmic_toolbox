# Uses python3
import sys


def get_change(m):

    rem_after_10 = m % 10
    num_tens = (m - rem_after_10)/10

    rem_after_5 = rem_after_10 % 5
    num_fives = (rem_after_10 - rem_after_5)/5

    num_ones = rem_after_5

    total_coins = num_tens + num_fives + num_ones

    return round(total_coins)


if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
