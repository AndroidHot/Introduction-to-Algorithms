"""
Matrix chain multiplication
"""

import numpy as np

INF = float('Inf')

# method 1: top-down with memoization
def memoized_matrix_chain(p):
    n = len(p) - 1
    m = np.full((n, n), INF)
    return lookup_chain(m, p, 0, n - 1)

def lookup_chain(m, p, i, j):
    if m[i][j] < INF:
        return m[i][j]
    if i == j:
        m[i][j] = 0
    else:
        for k in range(i, j):
            q = lookup_chain(m, p, i, k) + lookup_chain(m, p, k + 1, j) + p[i] * p[k+1] * p[j+1]
            if q < m[i][j]:
                m[i][j] = q
    return m[i][j]

# method 2: bottom-up method
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

# Exercise 15.2-2
def matrix_chain_multiply(arrays, s, i, j):
    if i == j:
        return arrays[i]
    else:
        A1 = matrix_chain_multiply(arrays, s, i, int(s[i][j] - 1))
        A2 = matrix_chain_multiply(arrays, s, int(s[i][j]), j)
        return np.dot(A1, A2)

if __name__ == '__main__':
    p = [5, 10, 3, 12, 5, 50, 6]
    m, s = matrix_chain_order(p)
    print(m)
    print(s)
    print_optimal_parens(s, 0, 5)
    print()
    arrays = [np.ones((5, 10)), np.ones((10, 3)), np.ones((3, 12)), np.ones((12, 5)), np.ones((5, 50)), np.ones((50, 6))]
    print(matrix_chain_multiply(arrays, s, 0, 5))
