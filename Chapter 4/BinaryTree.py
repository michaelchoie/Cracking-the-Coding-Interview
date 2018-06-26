# Create a binary tree, do BFS/DFS


class Queue(object):

    def __init__(self):
        self.values = []

    def enqueue(self, value):
        self.values.append(value)

    def dequeue(self):
        value = self.values[0]
        del self.values[0]

        return value


class Node(object):

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)


class BinaryTree(object):

    def __init__(self, root=None):
        self.root = root

    def bfs(self):
        queue = Queue()
        queue.enqueue(self.root)

        while len(queue.values) != 0:
            current = queue.dequeue()
            print(current, end=" ")
            if current.left:
                queue.enqueue(current.left)
            if current.right:
                queue.enqueue(current.right)

    def dfs(self, node, traversal):
        if not node:
            return False

        if traversal == "inorder":
            # Left, root, right
            if node.left:
                self.dfs(node.left, "inorder")
            print(node.value, end=" ")
            if node.right:
                self.dfs(node.right, "inorder")

        elif traversal == "preorder":
            # root, left, right
            print(node.value, end=" ")
            if node.left:
                self.dfs(node.left, "preorder")
            if node.right:
                self.dfs(node.right, "preorder")

        elif traversal == "postorder":
            # left, right, root
            if node.left:
                self.dfs(node.left, "postorder")
            if node.right:
                self.dfs(node.right, "postorder")
            print(node.value, end=" ")

        else:
            raise Exception("Not a valid traversal")


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)

    tree = BinaryTree(root)
    print()
    tree.bfs()
    print()

    print()
    tree.dfs(root, "inorder")
    print()
