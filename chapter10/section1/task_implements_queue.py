"""
Exercise 10.1-6

Two stacks implement the queue.
"""

from stack import Stack

class Queue(object):

    def __init__(self, length):
        self.stack1 = Stack(length)
        self.stack2 = Stack(length)

    def enqueue(self, element):
        try:
            self.stack1.push(element)
        except IndexError:
            raise IndexError('queue overflow.')

    def dequeue(self):
        while self.stack1.top > 0:
            self.stack2.push(self.stack1.pop())
        try:
            result = self.stack1.pop()
        except IndexError:
            raise IndexError('queue underflow.')
        while not self.stack2.stack_empty():
            self.stack1.push(self.stack2.pop())
        return result
