# Uses python3
import sys
import random

def partition3(a, l, r):
    pivot = a[l]
    lt = l
    rt = r
    i = l
    while i <= rt:
        if a[i] < pivot:
            a[i], a[lt] = a[lt], a[i]
            lt += 1
            i += 1
        elif a[i] > pivot:
            a[i], a[rt] = a[rt], a[i]
            rt -= 1
        else:
            i += 1
    return lt, rt

def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    #print(f'k:{k}')
    a[l], a[k] = a[k], a[l]

    #use partition3
    lt, rt = partition3(a, l, r)
    #print(f'a:{a}, left:{lt}, right:{rt}')
    randomized_quick_sort(a, l, lt - 1);
    randomized_quick_sort(a, rt + 1, r);

    return a

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    result = randomized_quick_sort(a, 0, n - 1)
    print(*result)


