#!/usr/bin/python3

class Node:
    """Defines a node of a singly linked list."""
    def __init__(self, data, next_node=None):
        """Initializes the node with a given data value and a next_node."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the node."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list."""
    def __init__(self):
        """Initializes the linked list with a head set to None."""
        self.__head = None

    def __str__(self):
        """String representation of the linked list."""
        current = self.__head
        node_values = []
        while current:
            node_values.append(str(current.data))
            current = current.next_node
        return "\n".join(node_values)

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position."""
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
            return

        if self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        while current.next_node and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node
