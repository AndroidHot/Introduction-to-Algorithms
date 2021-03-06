# 当数组 A[p..r] 中所有元素的值都相同时，PARTITION 返回的 q 值时什么？
# 答：返回的 q 值是 r

# 修改 PARTITION，使得当数组 A[p..r] 中所有元素的值都相同时，q = (p + r) / 2 向下取整。

import math

def partition(A, p, r):
    x = A[r]
    i = p - 1
    allElementsSame = True
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
            if A[j] != x:
                allElementsSame = False

    i = i + 1
    A[r] = A[i]
    A[i] = x
    if allElementsSame:
        i = math.floor((p + r) / 2)
    return i

def quicksort(A, p, r):
    if(p >= r):
        return
    q = partition(A, p, r)
    quicksort(A, p, q - 1)
    quicksort(A, q + 1, r)


if __name__ == '__main__':
    # array = [2, 8, 7, 1, 3, 5, 6, 4]
    array = [2, 2, 2, 2, 2, 2, 2, 2]

    quicksort(array, 0, len(array) - 1)
    print(array)
