"""
Minimum Priority Queue.
"""
import math

class MinimumPriorityQueue(object):

    def __init__(self, A):
        self.A = A
        self.__build_min_heap()

    def minimum(self):
        return self.A[0]

    def extract_min(self):
        min = self.A[0]
        self.A[len(self.A) - 1], self.A[0] = self.A[0], self.A[len(self.A) - 1]
        self.A = self.A[:len(self.A) - 1]
        self.__min_heapify(0)
        return min

    def decrease_key(self, i, key):
        if key > self.A[i]:
            raise ValueError('new key is bigger than current key.')
        self.A[i] = key
        while i > 0 and self.A[self.__parent_node(i)] > self.A[i]:
            self.A[self.__parent_node(i)], self.A[0] = self.A[0], self.A[self.__parent_node(i)]
            i = self.__parent_node(i)

    def insert(self, key):
        self.A.append(float('Inf'))
        self.decrease_key(len(self.A) - 1, key)

    def __parent_node(self, i):
        if i == 0:
            return
        parent_i = math.ceil(i / 2 - 1)
        return parent_i

    def __left_node(self, i):
        left_i = i * 2 + 1
        if left_i > len(self.A) - 1:
            return
        else:
            return left_i

    def __right_node(self, i):
        right_i = i * 2 + 2
        if right_i > len(self.A) - 1:
            return
        else:
            return right_i

    def __min_heapify(self, i):
        l = self.__left_node(i)
        r = self.__right_node(i)
        if l and self.A[l] <= self.A[i]:
            smallest = l
        else:
            smallest = i
        if r and self.A[r] <= self.A[smallest]:
            smallest = r
        if smallest != i:
            self.A[smallest], self.A[i] = self.A[i], self.A[smallest]
            if smallest <= len(self.A) / 2:
                self.__min_heapify(smallest)

    def __build_min_heap(self):
        for i in range(math.floor(len(self.A) / 2) - 1, -1, -1):
            self.__min_heapify(i)
