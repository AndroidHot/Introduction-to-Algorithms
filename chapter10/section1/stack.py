class Stack(object):

    def __init__(self, length):
        self.S = [None for _ in range(length)]
        self.top = -1

    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False

    def push(self, element):
        if self.top + 1 == len(self.S):
            raise IndexError('stack overflow')
        else:
            self.top = self.top + 1
            self.S[self.top] = element

    def pop(self):
        if self.is_empty():
            raise IndexError('stack underflow')
        else:
            self.top = self.top - 1
            return self.S[self.top + 1]
