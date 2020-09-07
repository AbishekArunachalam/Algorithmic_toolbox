#Uses python3

def calc_fib(n):
    value = list()
    for i in range(0, n+1):
        if i <= 1:
            value.append(i)
        else:
            cal = value[i-1] + value[i-2]
            print(cal)
            value.append(cal)
    return value[-1]


if __name__ == '__main__':
    n = int(input())
    result = calc_fib(n)
    print(result)