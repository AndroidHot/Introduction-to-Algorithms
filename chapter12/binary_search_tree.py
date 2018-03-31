'''
Binary Search Tree
'''

import sys
sys.path.insert(0, '/home/zhiwei/work/Introduction-to-Algorithms/chapter10/section1')
from stack import Stack

class BinarySearchTree(object):

    _inorder_walk_result = []

    def __init__(self, root_node = None):
        if root_node != None and not isinstance(root_node, BinarySearchTreeNode):
            raise ValueError('root_node is not BinarySearchTreeNode, please check!')
        self.root_node = root_node

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

    def tree_delete(self, node):
        if node.left == None:
            self.transplant(node.right, node)
        elif node.right == None:
            self.transplant(node.left, node)
        else:
            node_successor = self.tree_minimum(node.right)
            if node_successor.parent != node:
                self.transplant(node_successor.right, node_successor)
                node_successor.right = node.right
                node_successor.right.parent = node_successor
            self.transplant(node_successor, node)
            node_successor.left = node.left
            node_successor.left.parent = node_successor


    def transplant(self, from_node, into_node):
        if into_node.parent == None:
            self.root_node = from_node
        elif into_node == into_node.parent.left:
            into_node.parent.left = from_node
        else:
            into_node.parent.right = from_node
        if from_node != None:
            from_node.parent = into_node.parent

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
            self._inorder_walk_result.append(node.key)
            self.inorder_tree_walk(node.right)
        return self._inorder_walk_result

    def inorder_non_recursive(self, node):
        def push_nodes_to_stack(stack, node):
            while node:
                stack.push(node)
                node = node.left
        stack = Stack(len(self.inorder_tree_walk(self.root_node))) # param length can be easier to assign
        self._inorder_walk_result = []
        stack.push(node)
        push_nodes_to_stack(stack, node.left)
        while not stack.is_empty():
            pop_temp = stack.pop()
            self._inorder_walk_result.append(pop_temp.key)
            if pop_temp.right:
                push_nodes_to_stack(stack, pop_temp.right)
        return self._inorder_walk_result

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
