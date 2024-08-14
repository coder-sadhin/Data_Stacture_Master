
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


class LinkedListIterator:
    def __init__(self, head):
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        else:
            value = self.current.get_data()
            self.current = self.current.get_next()
            return value



if __name__ == "__main__":
    import doctest

    doctest.testmod()
