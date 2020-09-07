import numpy as np


# Uses python3
def edit_distance(s, t):
    s_len = len(s)
    t_len = len(t)

    dist_matrix = [[0 for x in range(t_len+1)] for y in range(s_len+1)]
    dist_matrix = np.array(dist_matrix)
    dist_matrix[:,0] = list(range(s_len+1))
    dist_matrix[0] = list(range(t_len+1))
    for i in range(1, s_len+1):
        for j in range(1, t_len+1):
            insertion = dist_matrix[i, j-1] + 1
            deletion = dist_matrix[i-1, j] + 1
            match = dist_matrix[i-1, j-1]
            mismatch = dist_matrix[i-1, j-1] + 1

            if s[i-1] == t[j-1]:
                dist_matrix[i][j] = min(insertion, deletion, match)
            else:
                dist_matrix[i][j] = min(insertion, deletion, mismatch)
    return int(dist_matrix[s_len, t_len])

if __name__ == "__main__":
    print(edit_distance(input(), input()))
