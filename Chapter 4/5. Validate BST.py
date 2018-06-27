"""Validate if binary tree is a BST."""
import unittest


class Node(object):

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def validate_bst(root, minimum=None, maximum=None):
    if not root:
        return True

    if (minimum and root.value <= minimum) or \
       (maximum and root.value > maximum):
            return False

    if not validate_bst(root.left, minimum, root.value) or \
       not validate_bst(root.right, root.value, maximum):
            return False

    return True


class Test(unittest.TestCase):

    def test_validate_bst(self):
        x = Node(5)
        x.left = Node(3)
        x.right = Node(6)
        x.left.left = Node(1)

        y = Node(1)
        y.left = Node(7)
        y.right = Node(4)

        self.assertTrue(validate_bst(x))
        self.assertFalse(validate_bst(y))


if __name__ == "__main__":
    unittest.main()
