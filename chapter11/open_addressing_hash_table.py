"""
Resolve conflicting hash table by open addressing.
Assume that the given keyword is a natural number. (x.key)
"""

from enum import Enum, unique
import random

class HashTable(object):

    def __init__(self, probe_sequence_type, slot_length):
        self.probe_sequence_type = probe_sequence_type
        self.slot_length = slot_length
        self.T = [None for _ in range(slot_length)]
        self.init_probe_param()

    # HASH-INSERT(T, k)
    def insert(self, k):
        i = 0
        while i != self.slot_length:
            j = self.cal_hash_value(k, i)
            if self.T[j] == None:
                self.T[j] = k
                return j
            else:
                i += 1
        raise IndexError('Hash table overflow.')

    # HASH-SEARCH(T, k)
    def search(self, k):
        i = 0
        j = -1
        while j == -1 or (self.T[j] != None and i != self.slot_length):
            j = self.cal_hash_value(k, i)
            if self.T[j] == k:
                return j
            i += 1
        return None

    def init_probe_param(self):
        # Quadratic probing  param.
        self.lp_c1 = random.randint(1, self.slot_length * 2)
        self.lp_c2 = random.randint(1, self.slot_length)

    def cal_hash_value(self, k, i):
        return {
            ProbeSequenceType.LinearProbing: self.linear_probing(k, i),
            ProbeSequenceType.QuadraticProbing: self.quadratic_probing(k, i),
            ProbeSequenceType.DoubleProbing: self.double_probing(k, i),
        }[self.probe_sequence_type]

    def linear_probing(self, k, i):
        return (self.auxiliary_hash_fun(k) + i) % self.slot_length

    def quadratic_probing(self, k, i):
        return (self.auxiliary_hash_fun(k) + self.lp_c1 * i + self.lp_c2 * i * i) % self.slot_length

    def double_probing(self, k, i):
        return (self.auxiliary_hash_fun(k) + i * self.auxiliary_hash_fun2(k)) % self.slot_length

    def auxiliary_hash_fun(self, k):
        return k % self.slot_length

    def auxiliary_hash_fun2(self, k):
        return (k % (self.slot_length - 1)) + 1


@unique
class ProbeSequenceType(Enum):
    LinearProbing = 0
    QuadraticProbing = 1
    DoubleProbing = 2
