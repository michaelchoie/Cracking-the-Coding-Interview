"""Create a linked list of all nodes at each depth of binary tree."""
"""TODO"""


class Node(object):

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)


class LinkedList(object):

    def __init__(self, values=None):
        self.head = None
        self.tail = None
        self.length = 0
        if values:
            self.add_multiple(values)

    def __len__(self):
        return self.length

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.right

    def __str__(self):
        values = [str(node) for node in self]
        return ' -> '.join(values)

    def add(self, value):
        if not isinstance(value, Node):
            value = Node(value)

        if not self.head:
            self.head = self.tail = value
        else:
            self.tail.right = value
            self.tail = value

        self.length += 1

        print(str(self.tail))

    def add_multiple(self, values):
        for node in values:
            self.add(node)


def bfs(root):
    linked_list = LinkedList()
    ref = []
    lists = []
    linked_list.add(root.value)
    ref.append(root)

    while len(linked_list) > 0:
        lists.append(linked_list)
        parents = ref

        linked_list = LinkedList()
        ref = []

        for parent in parents:
            if parent.left:
                linked_list.add(parent.left.value)
                ref.append(parent.left)
            if parent.right:
                linked_list.add(parent.right.value)
                ref.append(parent.right)

    return lists

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    lists = bfs(root)
    for linked_list in lists:
        print(linked_list)
