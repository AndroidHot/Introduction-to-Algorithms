"""
Red-black tree
"""

from enum import Enum, unique

class RedBlackTree(object):

    def __init__(self):
        self.nil = RedBlackTreeNode(None) # sentinel
        self.root_node = self.nil

    def insert(self, node):
        if not isinstance(node, RedBlackTreeNode):
            raise ValueError('insert node is not RedBlackTreeNode, please check!')
        y = self.nil
        x = self.root_node
        while x != self.nil:
            y = x
            if node.key <= x.key:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if y == self.nil:
            self.root_node = node
        elif node.key <= y.key:
            y.left = node
        else:
            y.right = node
        node.left = self.nil
        node.right = self.nil
        node.color = RBNodeColor.RED
        self.__insert_fixup(node)

    def __insert_fixup(self, node):
        def __fixup_case(node, y):
            if y.color == RBNodeColor.RED:
                node.parent.color = RBNodeColor.BLACK
                y.color = RBNodeColor.BLACK
                node.parent.parent.color = RBNodeColor.RED
                node = node.parent.parent
            else:
                if node == node.parent.right:
                    node = node.parent
                    self.left_rotate(node)
                node.parent.color = RBNodeColor.BLACK
                node.parent.parent.color = RBNodeColor.RED
                self.right_rotate(node.parent.parent)

        while node.parent.color == RBNodeColor.RED:
            if node.parent == node.parent.parent.left:
                y = node.parent.parent.right
                __fixup_case(node, y)
            else:
                y = node.parent.parent.left
                __fixup_case(node, y)
        self.root_node.color = RBNodeColor.BLACK

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

@unique
class RBNodeColor(Enum):
    BLACK = 0
    RED = 1
