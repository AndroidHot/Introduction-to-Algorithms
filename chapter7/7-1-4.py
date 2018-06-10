# 如何修改 QUICKSORT，使得它能够以非递增序进行排列。
def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        # Just need to change this line.
        if A[j] >= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
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


if __name__ == '__main__':
    # array = [2, 8, 7, 1, 3, 5, 6, 4]
    array = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]
    quicksort(array, 0, len(array) - 1)
    print(array)
