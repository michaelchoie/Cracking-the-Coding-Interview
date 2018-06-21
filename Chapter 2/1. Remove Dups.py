# First one - O(n); Second one - O(n^2)
from LinkedList import LinkedList


def remove_duplicates(llist):
    if llist.head is None:
        return

    node = llist.head
    logger = set([node.value])

    while node.next:
        if node.next.value in logger:
            node.next = node.next.next
        else:
            logger.add(node.next.value)
            node = node.next

    return llist


def follow_up(llist):
    if llist.head is None:
        return

    node = llist.head

    while node:
        tracker = node
        while tracker.next:
            if tracker.next.value == node.value:
                tracker.next = tracker.next.next
            else:
                tracker = tracker.next
        node = node.next

    return llist


def test():

    data = [(LinkedList([1, 1, 2, 2, 3, 4]),
             LinkedList([1, 2, 3, 4]))]

    for input_data, expected in data:
        print(remove_duplicates(input_data))
        print(expected)

    for input_data, expected in data:
        print(remove_duplicates(input_data)),
        print(expected)


if __name__ == "__main__":
    test()
