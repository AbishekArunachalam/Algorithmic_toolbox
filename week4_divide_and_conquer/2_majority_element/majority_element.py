# Uses python3
import sys
import numpy as np


# Function to find the candidate for Majority
def findCandidate(a):
    maj_index = 0
    count = 0
    for i in range(len(a)):
        if a[maj_index] == a[i]:
            count += 1
        else:
            count -= 1
        if count == 0:
            maj_index = i
            count = 1
    return a[maj_index]

def isMajority(A, cand):
    count = 0
    for i in range(len(A)):
        if A[i] == cand:
            count += 1
    if count > len(A)/2:
        return True
    else:
        return False


def get_majority_element(a, left, right):
    if left == right:
        return 0
    if left + 1 == right:
        return 1
    cand = findCandidate(a)
    if isMajority(a, cand) == True:
        return 1
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(get_majority_element(a, 0, n))