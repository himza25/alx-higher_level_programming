#!/usr/bin/python3
"""
A module containing a class definition
for a singly linked list and its nodes.
"""


class Node:
    """A class that defines a node in a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a Node object with data and next_node."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the data from the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the node."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the next_node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next_node."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """A class that defines a singly linked list."""

    def __init__(self):
        """Initialize an empty singly linked list."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position in the list."""
        new = Node(value)
        if self.__head is None:
            self.__head = new
            return

        if self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
            return

        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new.next_node = current.next_node
        current.next_node = new

    def __str__(self):
        """Return a string representation of the linked list."""
        values = []
        current = self.__head
        while current is not None:
            values.append(str(current.data))
            current = current.next_node
        return '\n'.join(values)


if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.sorted_insert(2)
    sll.sorted_insert(5)
    sll.sorted_insert(3)
    sll.sorted_insert(10)
    sll.sorted_insert(1)
    sll.sorted_insert(-4)
    sll.sorted_insert(-3)
    sll.sorted_insert(4)
    sll.sorted_insert(5)
    sll.sorted_insert(12)
    sll.sorted_insert(3)
    print(sll)
