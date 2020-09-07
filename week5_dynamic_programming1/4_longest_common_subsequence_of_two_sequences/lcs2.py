#Uses python3
import numpy
import sys

def lcs2(a, b):
    seq1_len = len(a)
    seq2_len = len(b)
    lcs_matrix = numpy.zeros((seq1_len + 1, seq2_len + 1))

    for i in range(1, seq1_len + 1):
        for j in range(1, seq2_len + 1):
            if a[i - 1] == b[j - 1]:
                lcs_matrix[i][j] = lcs_matrix[i - 1][j - 1] + 1
            if a[i - 1] != b[j - 1]:
                lcs_matrix[i][j] = max(lcs_matrix[i][j - 1], lcs_matrix[i - 1][j])

    return int(lcs_matrix[seq1_len][seq2_len])



    #write your code here
    return min(len(a), len(b))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
