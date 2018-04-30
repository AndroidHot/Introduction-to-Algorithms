"""
Huffman code
"""

import sys
sys.path.insert(0, '/home/zhiwei/work/Introduction-to-Algorithms/chapter6')
from minimum_priority_queue import MinimumPriorityQueue

def huffman(C):
    n = len(C)
    Q = MinimumPriorityQueue(C)
    for _ in range(n - 1):
        x = Q.extract_min()
        y = Q.extract_min()
        freq = x + y
        Q.insert(freq)
        print(freq)

if __name__ == '__main__':
    A = [45, 13, 12, 16, 9, 5]
    huffman(A)
