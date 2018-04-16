"""
Greedy algorithm - Activity selection problem
Assume that the input activity has been ordered by the end of time
"""

# Recursive greedy algorithm
def recursive_activity_selector(s, f, start, end):
    m = start + 1
    if start == -1:
        fx = 0
    else:
        fx = f[start]
    while m <= end and s[m] < fx:
        m += 1
    if m <= end:
        print(m)
        recursive_activity_selector(s, f, m, end)

# Iterative greedy algorithm
def greedy_activity_selector(s, f):
    A = [0]
    k = 0
    for j in range(1, len(s)):
        if s[j] >= f[k]:
            A.append(j)
            k = j
    return A

# Exercise 16.1-2
# Assume that the input activity has been ordered by the start of time
def greedy_activity_selector_exercise(s, f):
    end_index = len(f) - 1
    A = [end_index]
    k = end_index
    for j in range(end_index, -1, -1):
        if f[j] <= s[k]:
            A.append(j)
            k = j
    return A

if __name__ == '__main__':
    i = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    start_time = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    end_time = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
    # The expected results: 0, 3, 7, 10
    print(greedy_activity_selector(start_time, end_time))
    recursive_activity_selector(start_time, end_time, -1, len(i) - 1)

    # Exercise 16.1-2, the expected results: 10, 9, 5, 3
    start_time = [0, 1, 2, 3, 3, 5, 5, 6, 8, 8, 12]
    end_time = [6, 4, 14, 5, 9, 7, 9, 10, 11, 12, 16]
    print(greedy_activity_selector_exercise(start_time, end_time))
