# 快速排序的随机化版本，很多人都选择随机化版本的快速排序作为大数据输入情况下的排序算法。
import random

def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            exchangeElement(A, j, i)
    i = i + 1
    A[r] = A[i]
    A[i] = x
    return i

def randomized_partition(A, p, r):
    i = random.randint(p, r)
    exchangeElement(A, r, i)
    return partition(A, p, r)

def randomized_quicksort(A, p, r):
    if(p >= r):
        return
    q = randomized_partition(A, p, r)
    randomized_quicksort(A, p, q - 1)
    randomized_quicksort(A, q + 1, r)

def exchangeElement(Array, indexA, indexB):
    tempValue =  Array[indexA]
    Array[indexA] = Array[indexB]
    Array[indexB] = tempValue

# test
testArray = [2, 8, 7, 1, 3, 5, 6, 4]
testArray2 = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]
randomized_quicksort(testArray2, 0, len(testArray2) - 1)
print(testArray2)