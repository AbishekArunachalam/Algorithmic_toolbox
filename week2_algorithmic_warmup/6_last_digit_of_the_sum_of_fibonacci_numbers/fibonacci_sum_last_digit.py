# Uses python3


def fibonacci_sum_last_digit(n):
    current, next = 0, 1
    for i in range(n):
        current, next = next, (current+next) % 10
    return current


if __name__ == '__main__':
    n = int(input())
    print((fibonacci_sum_last_digit((n+2) % 60) + 9) % 10)
