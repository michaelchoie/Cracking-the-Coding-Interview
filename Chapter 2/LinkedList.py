"""Python implementation of a linked list"""


class Node(object):

    def __init__(self, value, nextNode=None, previousNode=None):
        self.value = value
        self.next = nextNode
        self.previous = previousNode

    def __str__(self):
        return str(self.value)


class LinkedList(object):

    def __init__(self, values=None):
        self.head = None
        self.tail = None
        if values is not None:
            self.add_multiple(values)

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def __str__(self):
        values = [str(x) for x in self]
        return ' -> '.join(values)

    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next

        return result

    def add(self, value):

        if not isinstance(value, Node):
            value = Node(value)

        if self.head is None:
            self.head = self.tail = value
        else:
            self.tail.next = value
            self.tail = self.tail.next

        return self.tail

    def add_multiple(self, values):
        for value in values:
            self.add(value)

    def add_to_beginning(self, value):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            self.head = Node(value, nextNode=self.head)

        return self.head


class DoublyLinkedList(LinkedList):

    def add(self, value):
        if self.head is None:
            self.head = self.tail = Node(value, None, self.tail)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

        return self
