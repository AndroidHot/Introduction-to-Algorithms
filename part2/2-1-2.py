# 快速排序（升序）
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

# 快速排序（降序）
def descend_order(array):
    A = array
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] < key:
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key
    return A

print(ascend_order([2, 1, 4, 3, 6, 5]))
print(descend_order([2, 1, 4, 3, 6, 5]))
