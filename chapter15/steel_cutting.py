"""
Dynamic programming algorithm, steel cutting problem
"""

# p is the price array, n is the length of steel bar, the return value is the biggest gains.

# method 1: top-down with memoization
def memoized_cut_rod(p, n):
    r = [None for _ in range(n + 1)]
    return memoized_cut_rod_aux(p, n, r)

def memoized_cut_rod_aux(p, n, r):
    if r[n] != None:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = float('-Inf')
        for i in range(n):
            q = max(q, p[i] + memoized_cut_rod_aux(p, n - i - 1, r))
    r[n] = q
    return q

# method 2: bottom-up method
def bottom_up_cut_rod(p, n):
    r = [None for _ in range(n + 1)]
    r[0] = 0
    for j in range(1, n + 1):
        q = float('-Inf')
        for i in range(j):
            q = max(q, p[i] + r[j - i - 1])
        r[j] = q
    return q

# test
p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
for i in range(1, 11):
    print(memoized_cut_rod(p, i))
    print(bottom_up_cut_rod(p, i))
