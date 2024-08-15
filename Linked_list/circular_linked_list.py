from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass
from typing import Any


@dataclass
class Node:
    data: Any
    next_node: Node | None = None


@dataclass
class CircularLinkedList:
    head: Node | None = None  # Reference to the head (first node)
    tail: Node | None = None  # Reference to the tail (last node)

    def __iter__(self) -> Iterator[Any]:
        """
        Iterate through all nodes in the Circular Linked List yielding their data.
        Yields:
            The data of each node in the linked list.
        """
        node = self.head
        while node:
            yield node.data
            node = node.next_node
            if node == self.head:
                break

    def __len__(self) -> int:
        """
        Get the length (number of nodes) in the Circular Linked List.
        """
        return sum(1 for _ in self)

    def __repr__(self) -> str:
        """
        Generate a string representation of the Circular Linked List.
        Returns:
            A string of the format "1->2->....->N".
        """
        return "->".join(str(item) for item in iter(self))

    def insert_tail(self, data: Any) -> None:
        """
        Insert a node with the given data at the end of the Circular Linked List.
        """
        self.insert_nth(len(self), data)

    def insert_head(self, data: Any) -> None:
        """
        Insert a node with the given data at the beginning of the Circular Linked List.
        """
        self.insert_nth(0, data)

    def insert_nth(self, index: int, data: Any) -> None:
        """
        Insert the data of the node at the nth pos in the Circular Linked List.
        Args:
            index: The index at which the data should be inserted.
            data: The data to be inserted.

        Raises:
            IndexError: If the index is out of range.
        """
        if index < 0 or index > len(self):
            raise IndexError("list index out of range.")
        new_node: Node = Node(data)
        if self.head is None:
            new_node.next_node = new_node  # First node points to itself
            self.tail = self.head = new_node
        elif index == 0:  # Insert at the head
            new_node.next_node = self.head
            assert self.tail is not None  # List is not empty, tail exists
            self.head = self.tail.next_node = new_node
        else:
            temp: Node | None = self.head
            for _ in range(index - 1):
                assert temp is not None
                temp = temp.next_node
            assert temp is not None
            new_node.next_node = temp.next_node
            temp.next_node = new_node
            if index == len(self) - 1:  # Insert at the tail
                self.tail = new_node

if __name__ == "__main__":
    import doctest

    doctest.testmod()
