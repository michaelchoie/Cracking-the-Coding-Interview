"""Implement SetOfStacks data structure."""
import unittest


class Node(object):

    def __init__(self, value):
        self.value = value
        self.above = None
        self.below = None

    def __str__(self):
        print(self.value)


class Stack(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.top = None
        self.bottom = None

    def push(self, value):
        if self.is_full():
            raise Exception("Stack is full")

        self.size += 1
        entry = Node(value)

        if self.size == 1:
            self.bottom = entry

        self.join(entry, self.top)
        self.top = entry

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")

        node = self.top
        self.top = self.top.below
        self.size -= 1

        return node.value

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def remove_bottom(self):
        node = self.bottom
        self.bottom = self.bottom.above

        if self.bottom:
            self.bottom.below = None

        self.size -= 1

        return node.value

    def join(self, top, old_top):
        if top:
            top.below = old_top
        if old_top:
            old_top.above = top


class SetOfStacks(object):

    def __init__(self, stack_size):
        self.stack_set = []
        self.stack_size = stack_size

    def last_stack(self):
        if not self.stack_set:
            return None

        return self.stack_set[-1]

    def push(self, value):
        last = self.last_stack()

        if last and last.is_full():
            new_stack = Stack(self.stack_size)
            new_stack.push(value)
            self.stack_set.append(new_stack)
        else:
            last.push(value)

    def pop(self):
        last = self.last_stack()
        value = last.pop()

        if last.is_empty():
            del self.stack_set[-1]

        return value

    def pop_at(self, index):
        return self.left_shift(index, remove_top=True)

    def left_shift(self, index, remove_top):
        stack = self.stack_set[index]
        removed_item = stack.pop() if remove_top else stack.remove_bottom()

        if stack.is_empty():
            del self.stack_set[index]
        elif len(self.stack_set) > index + 1:
            v = self.left_shift(index + 1, remove_top=False)
            stack.push(v)

        return removed_item


class Test(unittest.TestCase):

    stacks = SetOfStacks(2)
    stack1 = Stack(2)
    stack2 = Stack(2)
    stack3 = Stack(2)

    stack1.push(1)
    stack1.push(2)
    stack2.push(3)
    stack2.push(4)
    stack3.push(1)
    stack3.push(3)

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
