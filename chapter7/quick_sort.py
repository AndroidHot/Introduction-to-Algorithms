def quick_sort(A, p, r):
    if p >= r:
        return
    q = partition(A, p, r)
    quick_sort(A, p, q - 1)
    quick_sort(A, q + 1, r)

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
    quick_sort(array, 0, len(array) - 1)
    print(array)
