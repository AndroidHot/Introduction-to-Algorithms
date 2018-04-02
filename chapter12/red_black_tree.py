"""
Red-black tree
"""

class RedBlackTree(object):

    def __init__(self, root_node = None):
        self.nil = RedBlackTreeNode(None) # sentinel
        self.root_node = root_node

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root_node = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root_node = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.right = x
        x.parent = y

class RedBlackTreeNode(object):

    def __init__(self, key):
        self.key = key
        self.color= None
        self.parent = None
        self.left = None
        self.right = None
