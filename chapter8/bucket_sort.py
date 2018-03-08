import math
import random

def ascend_order(array):
    A = array
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key
    return A

def bucket_sort(A):
    n = len(A)
    B = [[] for _ in range(n)]
    for i in range(n):
        index = int(math.floor(n * A[i]))
        print(index)
        B[index].append(A[i])
    for i in range(n - 1):
        ascend_order(B[i])
    C = []
    for _B in B:
        for c in _B:
            C.append(c)
    return C

testArray = [random.random() for _ in range(10)]
print(bucket_sort(testArray))