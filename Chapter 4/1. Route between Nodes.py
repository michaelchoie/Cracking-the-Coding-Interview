"""Find whether there is a route between 2 nodes in a directed graph"""
import unittest


class Queue(object):

    def __init__(self):
        self.array = []

    def enqueue(self, value):
        self.array.append(value)

    def dequeue(self):
        if len(self.array) == 0:
            return False

        value = self.array[0]
        del self.array[0]

        return value


class Node(object):

    def __init__(self, value, adjacent=None):
        self.value = value
        self.visited = False
        if adjacent:
            self.adjacent = adjacent
        else:
            self.adjacent = []

    def add_neighbor(self, neighbor):
        if self.adjacent:
            self.adjacent.append(neighbor)
        else:
            self.adjacent = [neighbor]

    def add_neighbors(self, neighbors):
        for neighbor in neighbors:
            self.add_neighbor(neighbor)


class Graph(object):

    def __init__(self, nodes):
        if nodes:
            self.nodes = nodes
        else:
            self.nodes = []

    def breadth_first_search(self, root, target):
        queue = Queue()
        root.visited = True
        queue.enqueue(root)

        while len(queue.array) != 0:
            current = queue.dequeue()
            if current:
                adjacent = current.adjacent
                for neighbor in adjacent:
                    if not neighbor.visited:
                        if neighbor.value == target.value:
                            return True
                        else:
                            neighbor.visited = True
                            queue.enqueue(neighbor)

        return False


class Test(unittest.TestCase):

    def test_bfs(self):

        A = Node("A")
        B = Node("B")
        C = Node("C")
        D = Node("D")
        E = Node("E")

        A.add_neighbors([B, C])
        C.add_neighbor(D)

        graph = Graph([A, B, C, D, E])

        self.assertTrue(graph.breadth_first_search(A, C))
        self.assertFalse(graph.breadth_first_search(A, E))

if __name__ == "__main__":
    unittest.main()
