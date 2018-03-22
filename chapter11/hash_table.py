"""
Assume that the given keyword is a natural number. (x.key)
"""

from enum import Enum, unique
import math
import sys
sys.path.insert(0, '/home/zhiwei/work/Introduction-to-Algorithms/chapter10/section2')
from doubly_linked_list import DoublyLinkedList, DoublyLinkedListNode

class HashTable(object):

    def __init__(self, hash_func_type, slot_length):
        self.hash_func_type = hash_func_type
        self.slot_length = slot_length
        self.T = [DoublyLinkedList() for _ in range(slot_length)]

    # CHAINED-HASH-INSERT(T, x)
    def insert(self, x):
        if not isinstance(x, DoublyLinkedListNode):
            raise ValueError('node is not DoublyLinkedListNode, please check!')
        self.T[self.cal_hash_value(x.key)].insert(x)

    # CHAINED-HASH-SEARCH(T, x)
    def search(self, x):
        if not isinstance(x, DoublyLinkedListNode):
            raise ValueError('node is not DoublyLinkedListNode, please check!')
        return self.T[self.cal_hash_value(x.key)].search(x)

    # CHAINED-HASH-DELETE(T, x)
    def delete(self, x):
        if not isinstance(x, DoublyLinkedListNode):
            raise ValueError('node is not DoublyLinkedListNode, please check!')
        self.T[self.cal_hash_value(x.key)].delete(x)

    def cal_hash_value(self, value):
        return {
            HashFuncType.Division: value % self.slot_length,
        }[self.hash_func_type]


@unique
class HashFuncType(Enum):
    Division = 0
