"""
Exercise 10.1-7

Two queues implement the stack.
"""

from queue import Queue

class Stack(object):

    def __init__(self, length):
        self.queue1 = Queue(length)
        self.queue2 = Queue(length)
        self.usingQueue1Push = True

    def push(self, element):
        try:
            if self.usingQueue1Push:
                self.queue1.enqueue(element)
            else:
                self.queue2.enqueue(element)
        except IndexError:
            raise IndexError('stack overflow.')

    def pop(self):
        try:
            if self.usingQueue1Push:
                while not self.queue1.onlyOneElement():
                    self.queue2.enqueue(self.queue1.dequeue())
                result = self.queue1.dequeue()
            else:
                while not self.queue2.onlyOneElement():
                    self.queue1.enqueue(self.queue2.dequeue())
                result = self.queue2.dequeue()
        except IndexError:
            raise IndexError('stack underflow.')
        self.usingQueue1Push = not self.usingQueue1Push
        return result
