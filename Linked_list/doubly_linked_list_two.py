
class Node:
    def __init__(self, data: int, previous=None, next_node=None):
        self.data = data
        self.previous = previous
        self.next = next_node

    def __str__(self) -> str:
        return f"{self.data}"

    def get_data(self) -> int:
        return self.data

    def get_next(self):
        return self.next

    def get_previous(self):
        return self.previous

