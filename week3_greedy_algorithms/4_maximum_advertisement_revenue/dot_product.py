#Uses python3

import sys

def max_dot_product(a, b):
    a.sort(reverse= True)
    b.sort(reverse=True)
    result = a[0] * b[0]
    if len(a) == 1:
        return result
    for i in range(1, len(a)):
        result += a[i] * b[i]
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    
