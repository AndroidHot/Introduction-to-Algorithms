"""
Maximum Priority Queue.
"""
import math

class MaximumPriorityQueue(object):

    def __init__(self, A):
        self.A = A
        self.__build_max_heap()

    def maximum(self):
        return self.A[0]

    def extract_max(self):
        max = self.A[0]
        self.__exchangeElement(self.A, 0, len(self.A) - 1)
        self.A = self.A[:len(self.A) - 1]
        self.__max_heapify(0)
        return max

    def increase_key(self, i, key):
        if key < self.A[i]:
            raise ValueError('new key is smaller than current key.')
        self.A[i] = key
        while i > 0 and self.A[self.__parent_node(i)] < self.A[i]:
            self.__exchangeElement(self.A, i, self.__parent_node(i))
            i = self.__parent_node(i)

    def insert(self, key):
        self.A.append(float('-Inf'))
        self.increase_key(len(self.A) - 1, key)

    def __parent_node(self, i):
        if i == 0:
            print('self.A[0] no parent node.')
            return
        parent_i = int(math.ceil(i / 2 - 1))
        return parent_i

    def __left_node(self, i):
        left_i = i * 2 + 1
        if left_i > len(self.A) - 1:
            print('self.A[%d] no left node.' %i)
            return
        else:
            return left_i

    def __right_node(self, i):
        right_i = i * 2 + 2
        if right_i > len(self.A) - 1:
            print('self.A[%d] no right node.' %i)
            return
        else:
            return right_i

    def __max_heapify(self, i):
        l = self.__left_node(i)
        r = self.__right_node(i)
        if l and self.A[l] >= self.A[i]:
            largest = l
        else:
            largest = i
        if r and self.A[r] >= self.A[largest]:
            largest = r
        if largest != i:
            self.__exchangeElement(self.A, i, largest)
            if largest <= len(self.A) / 2:
                self.__max_heapify(largest)

    def __build_max_heap(self):
        for i in range(math.floor(len(self.A) / 2) - 1, -1, -1):
            self.__max_heapify(i)

    def __exchangeElement(self, Array, indexA, indexB):
        tempValue =  Array[indexA]
        Array[indexA] = Array[indexB]
        Array[indexB] = tempValue
