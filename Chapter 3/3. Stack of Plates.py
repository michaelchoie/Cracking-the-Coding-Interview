"""Implement SetOfStacks data structure."""
import unittest
from Stack import Stack


class SetOfStacks(object):

    def __init__(self, stack_size):
        self.stack_set = []
        self.stack_size = stack_size

    def last_stack(self):
        if not self.stack_set:
            return None

        return self.stack_set[-1]

    def push(self, value):
        if self.last_stack().is_full():
            new_stack = Stack(self.stack_size)
            new_stack.push(value)
            self.stack_set.append(new_stack)
        else:
            self.last_stack().push(value)

    def pop(self):
        value = self.last_stack().pop()

        if self.last_stack().is_empty():
            del self.stack_set[-1]

        return value

    def pop_at(self, index):
        value = self.stack_set[index].pop()

        return value


class Test(unittest.TestCase):

    stacks = SetOfStacks(2)
    stack1 = Stack(2)
    stack2 = Stack(2)

    stack1.push(1)
    stack1.push(2)
    stack2.push(3)
    stack2.push(4)

    stacks.stack_set.append(stack1)
    stacks.stack_set.append(stack2)

    def test_last_stack(self):
        self.assertEqual(self.stacks.last_stack(), self.stack2)

    def test_pop(self):
        self.stacks.pop()
        self.stacks.pop()
        self.assertEqual(self.stacks.pop(), 2)

    def test_pop_at(self):
        self.stacks.push(2)
        self.stacks.push(3)
        self.assertEqual(self.stacks.pop_at(0), 2)

if __name__ == "__main__":
    unittest.main()
