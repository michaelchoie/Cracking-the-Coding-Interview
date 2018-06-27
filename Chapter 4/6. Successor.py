"""Find the next node, in-order, of a given node in a BST."""
import unittest


class Node(object):

    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None


def successor(node):
    # in order means left, root, right

    if not node:
        return None

    if node.right:
        while node.left:
            node = node.left
        return node

    else:
        # go up until we're on the left side instead of the right
        current = node
        parent = current.parent
        while parent and parent.left != current:
            current = parent
            parent = parent.parent

        return parent


class Test(unittest.TestCase):

    def test_successor(self):
        x = Node(5)
        x.left = Node(3, x)
        x.right = Node(7, x)
        x.left.left = Node(2, x.left)
        x.left.right = Node(4, x.left)
        x.right.left = Node(6, x.right)
        x.right.right = Node(8, x.right)

        self.assertEqual(successor(x.right).value, x.right.left.value)

        x = Node(5)
        x.left = Node(3, x)
        x.right = Node(7, x)
        x.left.left = Node(2, x.left)
        x.left.right = Node(4, x.left)
        x.right.left = Node(6, x.right)
        x.right.right = Node(8, x.right)

        self.assertEqual(successor(x.left.right).value, x.value)

if __name__ == "__main__":
    unittest.main()
