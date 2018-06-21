"""Python implementation of a stack"""


class Stack(object):

    def __init__(self, stack_size, num_stacks=1):
        self.num_stacks = num_stacks
        self.array = [0] * (self.num_stacks * stack_size)
        self.size = [0] * self.num_stacks
        self.stack_size = stack_size

    def __str__(self):
        values = [str(x) for x in self.array]
        return ' '.join(values)

    def pop(self, nstack=0):
        if self.is_empty(nstack):
            raise Exception("Stack is empty")

        value = self.array[self.index_of_top(nstack)]
        self.array[self.index_of_top(nstack)] = 0
        self.size[nstack] -= 1

        return value

    def push(self, value, nstack=0):
        if self.is_full(nstack):
            raise Exception("Stack is full")

        self.size[nstack] += 1
        self.array[self.index_of_top(nstack)] = value

    def peek(self, nstack=0):
        if self.is_empty(nstack):
            raise Exception("Stack is empty")

        return self.array[self.index_of_top(nstack)]

    def is_empty(self, nstack=0):
        return self.size[nstack] == 0

    def is_full(self, nstack=0):
        return self.size[nstack] == self.stack_size

    def index_of_top(self, nstack=0):
        offset = nstack * self.stack_size - 1
        return self.size[nstack] + offset
