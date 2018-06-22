"""Implement a MyQueue class using 2 stacks"""
import unittest
from Stack import Stack


class Queue(object):

    def __init__(self, size):
        self.input_stack = Stack(size)
        self.output_stack = Stack(size)

    def __str__(self):
        stack1 = str(self.input_stack)
        stack2 = str(self.output_stack)
        return ', '.join([stack1, stack2])

    def enqueue(self, value):
        self.input_stack.push(value)

    def dequeue(self):
        if self.input_stack.is_empty() and self.output_stack.is_empty():
            raise Exception("Queue is empty")

        if self.output_stack.is_empty():
            while not self.input_stack.is_empty():
                value = self.input_stack.pop()
                self.output_stack.push(value)

        value = self.output_stack.pop()

        return value


class Test(unittest.TestCase):

    def test_enqueue_dequeue(self):
        queue = Queue(5)

        for x in range(5):
            queue.enqueue(x)

        for x in range(5):
            self.assertEqual(queue.dequeue(), x)


if __name__ == "__main__":
    unittest.main()
