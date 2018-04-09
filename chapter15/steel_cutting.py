"""
Dynamic programming algorithm, steel cutting problem

parameter value p is the price array, n is the length of steel bar.
return value r saves the maximum profit value, s saves the cut length of the first bar corresponding to the optimal solution.
"""

# method 1: top-down with memoization
def memoized_cut_rod(p, n):
    r = [None for _ in range(n + 1)]
    s = [None for _ in range(n + 1)]
    memoized_cut_rod_aux(p, n, r, s)
    return r, s

def memoized_cut_rod_aux(p, n, r, s):
    if r[n] != None:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = float('-Inf')
        for i in range(n):
            if q < p[i] + memoized_cut_rod_aux(p, n - i - 1, r, s):
                q = p[i] + memoized_cut_rod_aux(p, n - i - 1, r, s)
                s[n] = i + 1
    r[n] = q
    return q

# method 2: bottom-up method
def bottom_up_cut_rod(p, n):
    r = [None for _ in range(n + 1)]
    s = [None for _ in range(n + 1)]
    r[0] = 0
    for j in range(1, n + 1):
        q = float('-Inf')
        for i in range(j):
            if q < p[i] + r[j - i - 1]:
                q = p[i] + r[j - i - 1]
                s[j] = i + 1
        r[j] = q
    return r, s



"""
# test
p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
n = 10
r, s = bottom_up_cut_rod(p, n)
# r, s = memoized_cut_rod(p, n)
print(r)
print(s)
print('maximum profit value is %d.' % r[n])
print('Cutting plan is:')
while n > 0:
    print(s[n])
    n = n - s[n]
"""
