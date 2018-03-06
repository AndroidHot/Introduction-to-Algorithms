def counting_sort(A):
    B = [0 for _ in range(len(A))]
    C = []
    k = max(A)
    for _ in range(k + 1):
        C.append(0)
    for i in range(len(A)):
        C[A[i]] = C[A[i]] + 1
    for i in range(k + 1):
        if i != 0:
            C[i] = C[i] + C[i - 1]
    for j in range(len(A) - 1, -1, -1):
        B[C[A[j]] -1 ] = A[j]
        C[A[j]] = C[A[j]] - 1
    return B

testArray = [2, 5, 3, 0, 2, 3, 0, 3]
testArray2 = [6, 0, 2, 0, 1, 3, 4, 6, 1, 3, 2]
counting_sort(testArray2)