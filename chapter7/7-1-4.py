# 如何修改 QUICKSORT，使得它能够以非递增序进行排列。
def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        # Just need to change this line.
        if A[j] >= x:
            i = i + 1
            temp = A[j]
            A[j] = A[i]
            A[i] = temp
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

# test
testArray = [2, 8, 7, 1, 3, 5, 6, 4]
testArray2 = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]
quicksort(testArray2, 0, len(testArray2) - 1)
print(testArray2)