class Node(object):

    __slots__ = (
        'data',
        'next_node',
    )

    def __init__(self, data_=None, next_node=None):
        self.data = data_
        self.next_node = next_node

    def update_data(self, new_data):
        self.data = new_data

    def update_next(self, new_node):
        self.next_node = new_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node
