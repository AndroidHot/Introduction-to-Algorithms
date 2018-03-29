'''
Binary Search Tree
'''

class BinarySearchTree(object):

    left = 0
    right = 1

    def __init__(self, root_node = None):
        if root_node != None and not isinstance(root_node, BinarySearchTreeNode):
            raise ValueError('root_node is not BinarySearchTreeNode, please check!')
        self.root_node = root_node
        self._sip_node_parent = None

    def tree_insert(self, node):
        if not isinstance(node, BinarySearchTreeNode):
            raise ValueError('insert node is not BinarySearchTreeNode, please check!')
        y = None
        x = self.root_node
        while x != None:
            y = x
            if node.key <= x.key:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if y == None:
            self.root_node = node    # tree was empty
        elif node.key <= y.key:
            y.left = node
        else:
            y.right = node

    def tree_search(self, node, value):
        if node == None or value == node.key:
            return node
        return self.tree_search(node.left, value) if value <= node.key else self.tree_search(node.right, value)

    def iterative_tree_search(self, node, value):
        while node != None and value != node.key:
            if value <= node.key:
                node = node.left
            else:
                node = node.right
        return node

    def tree_minimum(self, node):
        while node != None:
            if node.left:
                node = node.left
            else:
                return node
        return node

    def tree_maximum(self, node):
        while node != None:
            if node.right:
                node = node.right
            else:
                return node
        return node

    def tree_successor(self, node):
        if node.right != None:
            return self.tree_minimum(node.right)
        y = node.parent
        while y != None and node == y.right:
            node = y
            y = y.parent
        return y

    def tree_predecessor(self, node):
        if node.left != None:
            return self.tree_maximum(node.left)
        y = node.parent
        while y != None and node == y.left:
            node = y
            y = y.parent
        return y

    def inorder_tree_walk(self, node):
        if node != None:
            self.inorder_tree_walk(node.left)
            print(node.key)
            self.inorder_tree_walk(node.right)

    def preorder_tree_walk(self, node):
        pass

    def postorder_tree_walk(self, node):
        pass


class BinarySearchTreeNode(object):

    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
