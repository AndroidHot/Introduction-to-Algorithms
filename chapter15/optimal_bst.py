"""
Optimal Binary Search Tree.
"""

import numpy as np

INF = float('Inf')

def optimal_bst(p, q, n):
    e = np.full((n + 1, n + 1), 0, float)
    w = np.full((n + 1, n + 1), 0, float)
    root = np.full((n, n), -1)
    for i in range(n + 1):
        e[i][i] = q[i]
        w[i][i] = q[i]
    for l in range(n):
        for i in range(n - l):
            j = i + l
            e[i][j+1] = INF
            w[i][j+1] = w[i][j] + p[j] + q[j+1]
            for r in range(i, j + 1):
                t = e[i][r] + e[r+1][j+1] + w[i][j+1]
                if t < e[i, j+1]:
                    e[i, j+1] = t
                    root[i, j] = r + 1
    return e, root


if __name__ == '__main__':
    p = [0.15, 0.1, 0.05, 0.1, 0.2]
    q = [0.05, 0.1, 0.05, 0.05, 0.05, 0.1]
    e, root = optimal_bst(p, q, len(p))
    print(e)
    print(root)
