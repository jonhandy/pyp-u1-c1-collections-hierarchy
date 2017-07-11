from .node import Node


class Sequenceable(object):
    def __init__(self):
        self.start = None
        self.end = None

    def get_elements(self):
        if not self.start:
            return []
        else:
            current_node = self.start
            
            lst = []
            lst.append(current_node.value)
            while current_node.next:
                current_node = current_node.next
                lst.append(current_node.value)
                
                
            return lst
                
            
                
            


class Appendable(object):
    def append(self, element):
        node = Node(element)
        if self.start is None:
            self.start = node
            self.end = node
        else:
            self.end.next = node
            self.end = node
            
        


class Popable(object):
    def pop(self):
        if self.start is None:
            raise IndexError
        
        val = self.start.value
        self.start = self.start.next
        return val
        


class Pushable:
    def push(self, element):
        node = Node(element)
        
        if self.start is None:
            self.start = node
            self.end = self.start
        else:
            node.next = self.start
            self.start = node
