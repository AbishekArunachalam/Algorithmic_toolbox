# Uses python3


def gcd(a, b):
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return a


if __name__ == "__main__":
    values = input()
    a, b = map(int, values.split())
    result = gcd(a, b)
    print(result)
