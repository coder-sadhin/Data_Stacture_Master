class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

    def __str__(self):
        return f"{self.data}"


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        """
        >>> linked_list = DoublyLinkedList()
        >>> linked_list.insert_at_head('b')
        >>> linked_list.insert_at_head('a')
        >>> linked_list.insert_at_tail('c')
        >>> tuple(linked_list)
        ('a', 'b', 'c')
        """
        node = self.head
        while node:
            yield node.data
            node = node.next

    def __str__(self):
        """
        >>> linked_list = DoublyLinkedList()
        >>> linked_list.insert_at_tail('a')
        >>> linked_list.insert_at_tail('b')
        >>> linked_list.insert_at_tail('c')
        >>> str(linked_list)
        'a->b->c'
        """
        return "->".join([str(item) for item in self])


if __name__ == "__main__":
    from doctest import testmod

    testmod()
