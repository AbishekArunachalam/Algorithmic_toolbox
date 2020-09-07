# python3
import sys
import math


def optimal_sequence(n):
    num_operations = [0, 0] + [math.inf] * (n - 1)

    for i in range(2, n + 1):
        temp1, temp2, temp3 = [math.inf] * 3

        temp1 = num_operations[i - 1] + 1
        if i % 2 == 0:
            temp2 = num_operations[i // 2] + 1
        if i % 3 == 0:
            temp3 = num_operations[i // 3] + 1
        min_ops = min(temp1, temp2, temp3)
        num_operations[i] = min_ops

    return num_operations


if __name__ == '__main__':

    input = sys.stdin.read()
    n = int(input)
    sequence = list(optimal_sequence(n))
    print(sequence[n])
    nums = [n]
    while n > 1:
        print(n)
        if n % 3 == 0 and sequence[n] - 1 == sequence[n // 3]:
            nums += [n // 3]
            n = n // 3
        elif n % 2 == 0 and sequence[n] - 1 == sequence[n // 2]:
            nums += [n // 2]
            n = n // 2
        else:
            nums += [n - 1]
            n = n - 1
    print(' '.join([str(i) for i in nums][::-1]))




