# Uses python3
import sys
import numpy

def optimal_weight(W, w):
    n = len(w)
    value_mat = numpy.zeros((W + 1, n + 1))

    for i in range(1, W + 1):
        for j in range(1, n + 1):
            value_mat[i, j] = value_mat[i, j - 1]
            if w[j - 1] <= i:
                temp = value_mat[i - w[j - 1],j - 1] + w[j - 1]
                if temp > value_mat[i, j]:
                    value_mat[i, j] = temp

    return (int(value_mat[W,  n]))


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
