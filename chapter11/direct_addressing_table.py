# direct addressing table

class DirectAddressingTable(object):

    def __init__(self, length):
        self.T = [None for _ in range(length)]
        self.length = length

    def search(self, k):
        if k < self.length and k >=  0:
            return self.T[k]
        else:
            raise IndexError('Directly addressed table out of bounds.')

    def insert(self, x):
        if not isinstance(x, DirectAddressingTableNode):
            raise ValueError('x is not DirectAddressingTableNode, please check!')            
        k = x.index
        if k < self.length and k >=  0:
            self.T[k] = x
        else:
            raise IndexError('Directly addressed table out of bounds.')

    def delete(self, x):
        if not isinstance(x, DirectAddressingTableNode):
            raise ValueError('x is not DirectAddressingTableNode, please check!')            
        k = x.index
        if k < self.length and k >=  0:
            self.T[k] = None                
        else:
            raise IndexError('Directly addressed table out of bounds.')

class DirectAddressingTableNode(object):

    def  __init__(self, index, data = None):
        self.index = index
        self.data = data
