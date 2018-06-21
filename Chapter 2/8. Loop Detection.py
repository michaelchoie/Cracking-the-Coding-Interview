from LinkedList import LinkedList


def loop_detector(ll):
    fast = slow = ll.head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow is fast:
            break

    if fast is None or fast.next is None:
        return None

    slow = ll.head
    while slow is not fast:
        slow = slow.next
        fast = fast.next

    return slow


def test():
    data = LinkedList(['a', 'b', 'c', 'd', 'e'])
    data.head.next.next.next.next.next = data.head.next.next

    return loop_detector(data)


if __name__ == "__main__":
    print(test())
