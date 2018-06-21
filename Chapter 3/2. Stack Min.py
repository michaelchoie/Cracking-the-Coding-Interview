# Create a stack that has push, pop, min in O(1)
import sys
import unittest
from Stack import Stack


class MinStack(Stack):

    def __init__(self, stack_size):
        super().__init__(stack_size)
        self.min_stack = Stack(stack_size)

    def push(self, value):
        if value <= self.min():
            self.min_stack.push(value)

        super().push(value)

    def pop(self):
        value = super().pop()
        if value == self.min():
            self.min_stack.pop()

    def min(self):
        if self.min_stack.is_empty():
            return sys.maxsize

        return self.min_stack.peek()


class Test(unittest.TestCase):

    def test_min_stack(self):
        data = MinStack(5)
        data.push(5)
        data.push(3)
        data.push(4)
        data.push(2)

        self.assertEqual(data.min(), 2)
        data.pop()
        self.assertEqual(data.min(), 3)


if __name__ == "__main__":
    unittest.main()
