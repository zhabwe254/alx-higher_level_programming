#!/usr/bin/python3
"""Module with a Node and SinglyLinkedList class."""


class Node:
    """A class that defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialization method with data and next_node."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the value of the data attribute."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the value of the data attribute."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the value of the next_node attribute."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the value of the next_node attribute."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """A class that defines a singly linked list."""

    def __init__(self):
        """Simple instantiation method."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position in the list."""
        new_node = Node(value)
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """Print the entire list in stdout."""
        result = ""
        current = self.__head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result[:-1]
