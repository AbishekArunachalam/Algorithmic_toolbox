#!usr/bin/env python3

import sys
import math


def get_change(m):
    if m == 1:
        return 1
    denominations = [1, 3, 4]
    min_coins = [0] + [math.inf] * m

    for i in range(1, m + 1):
        for j in denominations:
            if i >= j:
                coins = min_coins[i - j] + 1
                if coins < min_coins[i]:
                    min_coins[i] = coins
    return min_coins[m]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
