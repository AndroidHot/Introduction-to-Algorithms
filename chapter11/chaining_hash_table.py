"""
Resolve conflicting hash table by chaining.
Assume that the given keyword is a natural number. (x.key)
"""

from enum import Enum, unique
import math
import random
import sys
sys.path.insert(0, '/home/zhiwei/work/Introduction-to-Algorithms/chapter10/section2')
from doubly_linked_list import DoublyLinkedList, DoublyLinkedListNode

class HashTable(object):

    def __init__(self, hash_func_type, slot_length):
        self.hash_func_type = hash_func_type
        self.slot_length = slot_length
        self.T = [DoublyLinkedList() for _ in range(slot_length)]
        self.init_hash_method()

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

    def init_hash_method(self):
        # Multiply hash param.
        self.multiply_random_value = random.random()
        while self.multiply_random_value == 0:
            self.multiply_random_value = random.random()

        # Universal hash param.
        self.universal_P = 997 # Assuming all the keywords k to fall from 0 to (P - 1)
        self.universal_a = random.randint(1, self.universal_P - 1)
        self.universal_b = random.randint(0, self.universal_P - 1)

    def cal_hash_value(self, value):
        return {
            HashFuncType.Division: self.divide_hash_method(value),
            HashFuncType.Multiplication: self.multiply_hash_method(value),
            HashFuncType.Universal: self.universal_hash_method(value),
        }[self.hash_func_type]

    def divide_hash_method(self, value):
        return value % self.slot_length

    def multiply_hash_method(self, value):
        temp = value * self.multiply_random_value
        return int(math.floor(self.slot_length * (temp - math.floor(temp))))

    def universal_hash_method(self, value):
        return ((self.universal_a * value + self.universal_b) % self.universal_P) % self.slot_length


@unique
class HashFuncType(Enum):
    Division = 0
    Multiplication = 1
    Universal = 2
