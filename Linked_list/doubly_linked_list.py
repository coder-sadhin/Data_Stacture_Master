class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

    def __str__(self):
        return f"{self.data}"


if __name__ == "__main__":
    from doctest import testmod

    testmod()
