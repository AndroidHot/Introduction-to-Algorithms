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

def quicksort(A, p, r):
    if(p >= r):
        return
    q = partition(A, p, r)
    quicksort(A, p, q - 1)
    quicksort(A, q + 1, r)

def exchangeElement(Array, indexA, indexB):
    tempValue =  Array[indexA]
    Array[indexA] = Array[indexB]
    Array[indexB] = tempValue

# test
testArray = [2, 8, 7, 1, 3, 5, 6, 4]
testArray2 = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]
quicksort(testArray2, 0, len(testArray2) - 1)
print(testArray2)