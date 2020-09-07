# Uses python3
import sys
import numpy as np
import random

def binary_search(a, x):
    low, high = 0, len(a)-1
    while high >= low:
        mid_index = int(np.floor(low + ((high - low) / 2)))
        if x == a[mid_index]:
            return mid_index
        elif x < a[mid_index]:
            high = mid_index-1
        else:
            low = mid_index+1
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    a.sort()
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')
