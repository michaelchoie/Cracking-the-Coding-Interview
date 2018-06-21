from LinkedList import LinkedList


def intersection(ll1, ll2):
    if ll1.tail != ll2.tail:
        return False

    shorter = ll1 if len(ll1) <= len(ll2) else ll2
    longer = ll2 if len(ll1) <= len(ll2) else ll1

    strack = shorter.head
    ltrack = longer.head

    diff = len(longer) - len(shorter)

    for _ in range(diff):
        ltrack = ltrack.next

    while strack is not ltrack:
        strack = strack.next
        ltrack = ltrack.next

    return ltrack


def test():
    common = LinkedList([1, 2, 3])
    ll1 = LinkedList([4, 5, 6])
    ll2 = LinkedList([7, 8, 9])

    ll1.add_multiple(common)
    ll2.add_multiple(common)

    return intersection(ll1, ll2)


if __name__ == "__main__":
    print(test())
