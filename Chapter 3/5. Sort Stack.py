"""Sort a stack such that smallest items are on top."""
from Stack import Stack


def sort_min_stack(stack):
    temp_stack = Stack(stack.stack_size)
    while not stack.is_empty():
        temp_value = stack.pop()
        while not temp_stack.is_empty() and temp_value < temp_stack.peek():
            stack.push(temp_stack.pop())
        temp_stack.push(temp_value)

    return temp_stack


def sort_test():
    test = Stack(4)
    expected = Stack(4)
    test.push(2)
    test.push(1)
    test.push(3)
    test.push(4)

    for x in range(4):
        expected.push(x + 1)

    actual = sort_min_stack(test)

    print("Actual: ", actual)
    print("Expected: ", expected)


if __name__ == "__main__":
    sort_test()
