class Queue(object):

    def __init__(self, length):
        self.Q = [None for _ in range(length)]
        self.head = 0
        self.tail = 0
        self.maxIndex = length - 1

    def enqueue(self, element):
        if self._isOverFlow():
            raise IndexError('queue overflow.')
        else:
            self.Q[self.tail] = element
            if self.tail == self.maxIndex:
                self.tail = 0
            else:
                self.tail += 1

    def dequeue(self):
        if self._isUnderFlow():
            raise IndexError('queue underflow.')
        else:
            result = self.Q[self.head]
            self.Q[self.head] = None
            if self.head == self.maxIndex:
                self.head = 0
            else:
                self.head += 1
            return result

    def _isOverFlow(self):
        return (self.head == self.tail) and self.Q[self.head]

    def _isUnderFlow(self):
        return (self.head == self.tail) and (not self.Q[self.head])