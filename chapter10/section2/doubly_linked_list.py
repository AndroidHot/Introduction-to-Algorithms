# Doubly linked list

class DoublyLinkedList(object):

    def __init__(self):
        self.nil = DoublyLinkedListNode(None) # sentinel
        self.nil.prev = self.nil
        self.nil.next = self.nil

    def insert(self, node):
        if not isinstance(node, DoublyLinkedListNode):
            raise ValueError('node is not DoublyLinkedListNode, please check!')
        node.next = self.nil.next
        self.nil.next.prev = node
        self.nil.next = node
        node.prev = self.nil

    def delete(self, node):
        if not isinstance(node, DoublyLinkedListNode):
            raise ValueError('node is not DoublyLinkedListNode, please check!')
        delete_node = self.search(node)
        if delete_node == None:
            print('Have not found this node, do not remove any node.')
        else:
            delete_node.prev.next = delete_node.next
            delete_node.next.prev = delete_node.prev

    def delete_head(self):
        if self.is_empty():
            print('The Linked list is empty.')
            return None
        else:
            result = self.nil.next
            self.nil.next = result.next
            result.next.prev = self.nil
            return result

    def delete_tail(self):
        if self.is_empty():
            print('The Linked list is empty.')
            return None
        else:
            result = self.nil.prev
            self.nil.prev = result.prev
            result.prev.next = self.nil
            return result

    def search(self, node):
        if not isinstance(node, DoublyLinkedListNode):
            raise ValueError('node is not DoublyLinkedListNode, please check!')
        result = self.nil.next
        while result != self.nil and (result.key != node.key or result.prev != node.prev or result.next != node.next):
            result = result.next
        return result if result != self.nil else None

    def is_empty(self):
        return self.nil.next == self.nil

    def visual(self):
        # {prev : xxx, self : xxx, key : xxx, next : xxx}
        visual_text = '{\n prev : ' + str(self.nil.prev) + ',\n self : ' + str(self.nil) + ',\n key : nil'
        x = self.nil.next
        while x != self.nil:
            _visual_text = ',\n next : ' + str(x) + '\n}\n->\n{\n prev : ' + str(x.prev) + '\n self : ' + str(x) +',\n key : ' + str(x.key)
            visual_text += _visual_text
            x = x.next
        visual_text += (',\n next : ' + str(self.nil) +'\n}')
        return visual_text

class DoublyLinkedListNode(object):

    def __init__(self, key):
        self.prev = None
        self.key = key
        self.next = None
