# 快速排序的随机化版本，很多人都选择随机化版本的快速排序作为大数据输入情况下的排序算法。
import random

def randomized_quick_sort(A, p, r):
    if p >= r:
        return
    q = randomized_partition(A, p, r)
    randomized_quick_sort(A, p, q - 1)
    randomized_quick_sort(A, q + 1, r)

def randomized_partition(A, p, r):
    i = random.randint(p, r)
    A[i], A[r] = A[r], A[i]
    return partition(A, p, r)

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


if __name__ == '__main__':
    array = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]
    randomized_quick_sort(array, 0, len(array) - 1)
    print(array)
