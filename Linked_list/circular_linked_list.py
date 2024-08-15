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

if __name__ == "__main__":
    import doctest

    doctest.testmod()
