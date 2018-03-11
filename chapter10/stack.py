class Stack(object):

    def __init__(self, length):
        self.S = [None for _ in range(length)]
        self.top = -1

    def stack_empty(self):
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
        if self.stack_empty():
            raise IndexError('stack underflow')
        else:
            self.top = self.top - 1
            return self.S[self.top + 1]


# test
s = Stack(5)
print(s.stack_empty()) # True
s.push(1)
s.push(22)
s.push(333)
print(s.pop()) # 333
print(s.pop()) # 22
s.push(4444)
s.push(55555)
print(s.pop()) # 55555
print(s.pop()) # 4444
print(s.stack_empty()) # False
print(s.pop()) # 1
print(s.stack_empty()) # True
