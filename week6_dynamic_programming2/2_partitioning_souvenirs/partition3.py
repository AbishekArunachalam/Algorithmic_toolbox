# Uses python3
import sys
import numpy

def partition3(W, n, A):
    count = 0
    value = numpy.zeros((W+1, n+1))
    for i in range(1, W+1):
        for j in range(1, n+1):
            value[i, j] = value[i, j-1]
            if A[j-1]<=i:
                temp = value[i-A[j-1], j-1] + A[j-1]
                if temp > value[i][j]:
                    value[i][j] = temp
            if value[i][j] == W:
                count += 1

    if count < 3:
        return  0
    else:
        return 1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    total_weight = sum(A)
    if sum(A)%3 !=0:
        print(0)
    elif n < 3:
        print(0)
    else:
        print(partition3(total_weight//3, n, A))

