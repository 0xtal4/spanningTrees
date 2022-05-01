class Node:
    def __init__(self, _key, _data, _next):
        self.next = _next
        self.data = _data

    def get_next(self):
        return self.next
    def get_data(self):
        return self.data
    def set_next(self, _next):
        self.next = _next
