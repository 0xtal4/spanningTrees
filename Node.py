class Node():
    def __init__(self, _key, _next):
        self.next = _next
        self.key = _key

    def get_next(self):
        return self.next

    def set_next(self, _next):
        self.next = _next
