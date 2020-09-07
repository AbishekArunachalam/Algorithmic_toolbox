#Uses python3
import numpy
import sys

def lcs3(a, b, c):
    seq1_len = len(a)
    seq2_len = len(b)
    seq3_len = len(c)

    lcs_matrix = numpy.zeros((seq1_len + 1, seq2_len + 1, seq3_len + 1))

    for i in range(1, seq1_len + 1):
        for j in range(1, seq2_len + 1):
            for k in range(1, seq3_len + 1):
                if a[i - 1] == b[j - 1] == c[k - 1]:
                    lcs_matrix[i][j][k] = lcs_matrix[i - 1][j - 1][k - 1] + 1
                else:
                    lcs_matrix[i][j][k] = max(lcs_matrix[i - 1][j][k], lcs_matrix[i][j - 1][k], lcs_matrix[i][j][k - 1])

    return int(lcs_matrix[i, j, k])


    #write your code here
    return min(len(a), len(b), len(c))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
