# Use one array to implement three stacks
import unittest


class ThreeInOne(object):

    def __init__(self, stack_size):
        self.num_stacks = 3
        self.array = [0] * (self.num_stacks * stack_size)
        self.size = [0] * self.num_stacks
        self.stack_size = stack_size

    def pop(self, nstack):
        if self.is_empty(nstack):
            raise Exception("Stack is empty")

        value = self.array[self.index_of_top(nstack)]
        self.array[self.index_of_top(nstack)] = 0
        self.size[nstack] -= 1

        return value

    def push(self, nstack, value):
        if self.is_full(nstack):
            raise Exception("Stack is full")

        self.size[nstack] += 1
        self.array[self.index_of_top(nstack)] = value

    def peek(self, nstack):
        if self.is_empty(nstack):
            raise Exception("Stack is empty")

        return self.array[self.index_of_top(nstack)]

    def is_empty(self, nstack):
        return self.size[nstack] == 0

    def is_full(self, nstack):
        return self.size[nstack] == self.stack_size

    def index_of_top(self, nstack):
        offset = nstack * self.stack_size - 1
        return self.size[nstack] + offset


class Test(unittest.TestCase):

    def test(self):
        data = ThreeInOne(2)
        data.push(0, 5)
        data.push(0, 8)
        data.push(1, 5)

        self.assertTrue(data.is_full(0))
        self.assertEqual(data.pop(0), 8)
        self.assertTrue(data.is_empty(2))
        self.assertEqual(data.index_of_top(1), 2)


if __name__ == "__main__":
    unittest.main()
