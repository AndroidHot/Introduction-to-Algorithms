import math

def parent_node(A, i):
    if i == 0:
        print('A[0] no parent node.')
        return
    parent_i = math.ceil(i / 2 - 1)
    return parent_i

def left_node(A, i):
    left_i = i * 2 + 1
    if left_i > len(A) - 1:
        print('A[%d] no left node.' %i)
        return
    else:
        return left_i
        
def right_node(A, i):
    right_i = i * 2 + 2
    if right_i > len(A) - 1:
        print('A[%d] no right node.' %i)
        return
    else:
        return right_i

def max_heapify(A, i):
    l = left_node(A, i)
    r = right_node(A, i)
    if l and A[l] >= A[i]:
        largest = l
    else:
        largest = i
    if r and A[r] >= A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        if largest <= len(A) / 2:
            max_heapify(A, largest)

def min_heapify(A, i):
    l = left_node(A, i)
    r = right_node(A, i)
    if l and A[l] <= A[i]:
        smallest = l
    else:
        smallest = i
    if r and A[r] <= A[smallest]:
        smallest = r
    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        if smallest <= len(A) / 2:
            min_heapify(A, smallest)

def build_max_heap(A):
    for i in range(math.floor(len(A) / 2) - 1, -1, -1):
        max_heapify(A, i)

def build_min_heap(A):
    for i in range(math.floor(len(A) / 2) - 1, -1, -1):
        min_heapify(A, i)

def heapsort(A):
    build_max_heap(A)
    B = []
    for i in range(len(A) - 1, 0, -1):
        value = A[0]
        A[i], A[0] = A[0], A[i]
        A = A[:i]
        B.append(value)
        max_heapify(A, 0)
    B.append(A[0])
    B.reverse()
    return B


if __name__ == '__main__':
    array1 = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    array2 = [5, 13, 2, 25, 7, 17, 20, 8, 4]

    result = heapsort(array2)
    print(result)
