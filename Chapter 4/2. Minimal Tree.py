"""Given sorted array, create a BST with minimal height."""


class Node(object):

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def arrayToBST(array, start, end):
    if start > end:
        return False

    middle = int((start + end) / 2)
    root = Node(array[middle])
    root.left = arrayToBST(array, start, middle - 1)
    root.right = arrayToBST(array, middle + 1, end)

    return root


def in_order_dfs(node):
    # Left, Root, Right
    if not node:
        return False

    if node.left:
        in_order_dfs(node.left)
    print(node.value, end=" ")
    if node.right:
        in_order_dfs(node.right)


if __name__ == "__main__":
    array = [1, 5, 2, 4, 6, 10, 3, 2, 5, 9, 10]
    sorted_array = [1, 2, 3, 4, 5, 6, 7]
    bst = arrayToBST(sorted_array, 0, len(sorted_array) - 1)
    in_order_dfs(bst)
