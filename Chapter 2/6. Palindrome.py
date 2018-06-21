import unittest
from LinkedList import LinkedList


def palindrome(ll):

    slow = fast = ll.head
    stack = []

    if slow is None:
        return False

    while fast and fast.next:
        stack.append(slow.value)
        slow = slow.next
        fast = fast.next.next

    if fast is not None:
        slow = slow.next

    while slow:
        if stack.pop() != slow.value:
            return False

        slow = slow.next

    return True


class Test(unittest.TestCase):

    data = [(LinkedList([1, 2, 3, 2, 1]), True),
            (LinkedList([1, 2, 2, 1]), True),
            (LinkedList([1, 2, 3]), False),
            (LinkedList(), False)]

    def test_palindrome(self):
        for ll, expected in self.data:
            self.assertEqual(palindrome(ll), expected)

if __name__ == "__main__":
    unittest.main()
