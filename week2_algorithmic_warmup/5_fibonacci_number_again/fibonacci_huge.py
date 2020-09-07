# Uses python3

def get_fibonacci_huge(n, m):

    previous = 0
    current = 1
    if n in [1,2]:
        return 1

    mod_values = [previous, current]
    for i in range(2, n*m+1):
        previous, current = current, (previous + current)
        remainder = current % m
        mod_values.append(remainder)
        if mod_values[i] == 1 and mod_values[i-1] == 0 and i > 2:
            mod_values = mod_values[: len(mod_values) - 2]
            list_len = len(mod_values)
            index = n%list_len
            return mod_values[index]


if __name__ == '__main__':
    values = input()
    n, m = map(int, values.split())
    print(get_fibonacci_huge(n, m))
