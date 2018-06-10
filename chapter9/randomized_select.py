# -*- coding: utf-8 -*-
# 期望为线性时间的选择算法，返回数组 A[p..r] 中第 i 小的元素(假设输入数据都是互异的)。
import random

def randomized_select(A, p, r, i):
    if p == r:
        return A[p]
    q = randomized_partition(A, p, r)
    k = q - p + 1
    if i == k:
        return A[q]
    elif i < k:
        return randomized_select(A, p, q - 1, i)
    else:
        return randomized_select(A, q + 1, r, i - k)

def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    i = i + 1
    A[r] = A[i]
    A[i] = x
    return i

def randomized_partition(A, p, r):
    i = random.randint(p, r)
    A[i], A[r] = A[r], A[i]
    return partition(A, p, r)


if __name__ == '__main__':
    array = [3, 2, 9, 0, 7, 5, 4, 8, 6, 1]
    print(2 == randomized_select(array, 0, len(array) - 1, 3))
