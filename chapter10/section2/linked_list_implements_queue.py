"""
Exercise 10.2-3

One doubly linked list implement the queue.
"""

from doubly_linked_list import DoublyLinkedList, DoublyLinkedListNode

class Queue(object):

    def __init__(self):
        self.Q = DoublyLinkedList()

    def enqueue(self, element):
        self.Q.insert(DoublyLinkedListNode(element))

    def dequeue(self):
        tail_node = self.Q.delete_tail()
        if tail_node:
            return tail_node.key
        else:
            raise('Queue underflow.')

    def is_empty(self):
        return self.Q.is_empty()
