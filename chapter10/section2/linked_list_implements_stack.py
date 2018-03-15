"""
Exercise 10.2-2

One singly linked list implement the stack.
"""

from singly_linked_list import SinglyLinkedList, SinglyLinkedListNode

class Stack(object):

    def __init__(self):
        self.S = SinglyLinkedList()

    def stack_empty(self):
        if self.S.nil.next == self.S.nil:
            return True
        else:
            return False

    def push(self, element):
        self.S.insert(SinglyLinkedListNode(element)) # Linked list implementation of stack overflow do not exist

    def pop(self):
        head_node = self.S.delete_head()
        if head_node:
            return head_node.key
        else:
            raise IndexError('stack underflow')
