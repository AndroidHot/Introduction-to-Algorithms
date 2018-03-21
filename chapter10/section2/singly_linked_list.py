# Singly linked list

class SinglyLinkedList(object):

    def __init__(self):
        self.nil = SinglyLinkedListNode(None) # sentinel
        self.nil.next = self.nil

    def insert(self, node):
        if not isinstance(node, SinglyLinkedListNode):
            raise ValueError('node is not SinglyLinkedListNode, please check!')
        node.next = self.nil.next
        self.nil.next = node

    def delete(self, node):
        if not isinstance(node, SinglyLinkedListNode):
            raise ValueError('node is not SinglyLinkedListNode, please check!')
        previous_node = self.search_previous_node(node)
        if previous_node == None:
            print('Have not found this node, do not remove any node.')
        else:
            previous_node.next = node.next

    def delete_head(self):
        if self.is_empty():
            print('The Linked list is empty.')
            return None
        else:
            result = self.nil.next
            self.nil.next = result.next
            return result

    def search(self, node):
        if not isinstance(node, SinglyLinkedListNode):
            raise ValueError('node is not SinglyLinkedListNode, please check!')
        result = self.nil.next
        while result != self.nil and (result.key != node.key or result.next != node.next):
            result = result.next
        return result if result != self.nil else None

    def search_previous_node(self, node):
        if not isinstance(node, SinglyLinkedListNode):
            raise ValueError('node is not SinglyLinkedListNode, please check!')
        x = self.nil.next
        result = self.nil
        while x != self.nil and (x.key != node.key or x.next != node.next):
            result = x
            x = x.next
        return result if x != self.nil else None

    def is_empty(self):
        return self.nil.next == self.nil

    def visual(self):
        # {self : xxx, key : xxx, next : xxx}
        visual_text = '{\n self : ' + str(self.nil) + ',\n key : nil'
        x = self.nil.next
        while x != self.nil:
            _visual_text = ',\n next : ' + str(x) + '\n}\n->\n{\n self : ' + str(x) +',\n key : ' + str(x.key)
            visual_text += _visual_text
            x = x.next
        visual_text += (',\n next : ' + str(self.nil) +'\n}')
        return visual_text

class SinglyLinkedListNode(object):

    def __init__(self, key):
        self.key = key
        self.next = None
