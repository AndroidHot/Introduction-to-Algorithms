"""
Greedy algorithm - Fractional knapsack problem
"""

def greedy_fractional_knapsack(v, w, W):
    e = [v[i] / w[i] for i in range(len(v))]
    free_W = W
    result = []
    index = e.index(max(e))
    while free_W > 0:
        if w[index] <= free_W:
            result.append('all goods %d' % index)
            free_W -= w[index]
            e[index] = float('-Inf')
            index = e.index(max(e))
        else:
            result.append('%s / %s goods %s' % (free_W, w[index], index))
            free_W -= free_W
    return result

if __name__ == '__main__':
    v = [60, 120, 100]
    w = [10, 30, 20]
    W = 50
    print(greedy_fractional_knapsack(v, w, W))
