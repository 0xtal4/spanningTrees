import Node


class LinkedList:
    def __init__(self, _head):
        self.head = _head

    def add_last(self, node):
        pos = self.head
        while pos.get_next() is not None:
            pos = pos.get_next()
        pos.set_next(node)
    def replace_node(self, data):
        pos = self.head
        while pos.get_next() is not None:
            if pos.get_data()[0] == data[0]:
                pos.set_data(data)
                return True
        return False


