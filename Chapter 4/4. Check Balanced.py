"""Check to see if a binary tree is balanced."""
import unittest


class Node(object):

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)


def height(root):

    if not root:
        return 0
    return max(height(root.left), height(root.right)) + 1


def isBalanced(root):

    if not root:
        return True

    left = height(root.left)
    right = height(root.right)

    if abs(left - right) <= 1 and isBalanced(root.left) \
       and isBalanced(root.right):
        return True

    return False


class Test(unittest.TestCase):

    def test_is_balanced(self):
        x = Node(1)
        x.left = Node(2)
        x.right = Node(3)
        x.left.left = Node(4)
        x.left.left.left = Node(5)

        y = Node(1)
        y.left = Node(2)
        y.right = Node(3)
        y.left.left = Node(4)
        y.left.right = Node(5)

        self.assertFalse(isBalanced(x))
        self.assertTrue(isBalanced(y))


if __name__ == "__main__":
    unittest.main()
