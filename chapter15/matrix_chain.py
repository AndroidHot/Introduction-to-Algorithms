"""
Matrix chain multiplication
"""

import numpy as np

def matrix_chain_order(p):
    n = len(p) - 1
    m = np.zeros((n, n)) # m save optimal value
    s = np.zeros((n, n)) # s Stores the segmentation point k corresponding to the optimal value m
    for l in range(1, n):
        for i in range(n - l):
            j = i + l
            m[i][j] = float('Inf')
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i] * p[k+1] * p[j+1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k + 1
    return m, s

def print_optimal_parens(s, i, j):
    if i == j:
        print('A', end='')
    else:
        print('(', end='')
        print_optimal_parens(s, i, int(s[i][j] - 1))
        print_optimal_parens(s, int(s[i][j]), j)
        print(')', end='')

if __name__ == '__main__':
    p = [30, 35, 15, 5, 10, 20, 25]
    m, s = matrix_chain_order(p)
    print(m)
    print(s)
    print_optimal_parens(s, 0, 5)
