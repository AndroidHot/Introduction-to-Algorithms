"""
longest common subsequence problem.
"""
import numpy as np

LEFT = '←'
UP = '↑'
UPPERLEFT = '↖'

# Calculate the length of longest common subsequence.
def lcs_length(X, Y):
    m = len(X)
    n = len(Y)
    c = np.full((m + 1, n + 1), 0)
    b = np.full((m + 1, n + 1), ' ')
    for i in range(m):
        for j in range(n):
            if X[i] == Y[j]:
                c[i][j] = c[i-1][j-1] + 1
                b[i][j] = UPPERLEFT
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = UP
            else:
                c[i][j] = c[i][j-1]
                b[i][j] = LEFT
    return c, b

# Exercise 15.4-3 top-down with memoization
def memoized_lcs_length(X, Y):
    m = len(X)
    n = len(Y)
    c = np.full((m, n), -1)
    return lookup_lcs_length(X, Y, c, m - 1, n - 1)

def lookup_lcs_length(X, Y, c, i, j):
    if c[i][j] > -1:
        return c[i][j]
    if i == -1 or j == -1:
        c[i][j] = 0
    else:
        if X[i] == Y[j]:
            c[i][j] = lookup_lcs_length(X, Y, c, i - 1, j - 1) + 1
        else:
            c[i][j] = max(lookup_lcs_length(X, Y, c, i - 1, j), lookup_lcs_length(X, Y, c, i, j - 1))
    return c[i][j]

# Construction longest common subsequence.
def print_lcs(b, X, i, j):
    if i == -1 or j == -1:
        return
    if b[i,j] == UPPERLEFT:
        print_lcs(b, X, i - 1, j - 1)
        print(X[i])
    elif b[i][j] == LEFT:
        print_lcs(b, X, i, j - 1)
    else:
        print_lcs(b, X, i - 1, j)

if __name__ == '__main__':
    X = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
    Y = ['B', 'D', 'C', 'A', 'B', 'A']
    c, b = lcs_length(X, Y)
    print(c)
    print(b)
    print_lcs(b, X, len(X) - 1, len(Y) - 1)
    print(memoized_lcs_length(X, Y))
