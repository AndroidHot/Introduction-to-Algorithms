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

    def delete(self, value):
        previous_node = self.search_previous_node(value)
        current_node = self.search(value)
        if previous_node == None:
            print('Have not found this node, do not remove any node.')
        else:
            previous_node.next = current_node.next

    def search(self, value):
        result = self.nil.next
        while result != self.nil and result.key != value:
            result = result.next
        return result if result != self.nil else None

    def search_previous_node(self, value):
        x = self.nil.next
        result = self.nil
        while x != self.nil and x.key != value:
            result = x
            x = x.next
        return result if x != self.nil else None

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
