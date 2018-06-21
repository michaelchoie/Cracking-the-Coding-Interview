# O(n)
import unittest
from LinkedList import LinkedList


def kth_to_last(llist, k):
    tracker = llist.head
    if k > len(llist):
        return None

    for _ in range(len(llist) - k):
        tracker = tracker.next

    return tracker.value


class Test(unittest.TestCase):

    data = [(LinkedList([1, 2, 3]), 2, 2),
            (LinkedList([1, 2, 3, 4, 5]), 3, 3),
            (LinkedList(), 3, None)]

    def test_kth_to_last(self):
        for llist, k, expected in self.data:
            self.assertEqual(kth_to_last(llist, k), expected)


if __name__ == "__main__":
    unittest.main()
