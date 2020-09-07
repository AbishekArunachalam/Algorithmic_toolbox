# Uses python3

def lcm(a,b):
    max_num = max(a, b)
    if a != max_num:
        min_num = a
    else:
        min_num = b

    for i in range(1, min_num+1):
        temp = max_num*i
        if temp % min_num == 0:
            return temp
    return a*b


if __name__ == '__main__':
    values = input()
    a, b = map(int, values.split())
    result = lcm(a, b)
    print(result)
