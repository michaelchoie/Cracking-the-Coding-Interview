from LinkedList import LinkedList


def sum_lists(ll1, ll2):

    current1, current2 = ll1.head, ll2.head
    carry = 0
    ll = LinkedList()

    while current1 or current2:
        total = carry

        if current1:
            total += current1.value
            current1 = current1.next
        if current2:
            total += current2.value
            current2 = current2.next

        ll.add(total % 10)
        carry = total // 10

    if carry:
        ll.add(carry)

    return ll


def follow_up(ll1, ll2):

    if len(ll1) > len(ll2):
        for _ in range(len(ll1) - len(ll2)):
            ll2.add_to_beginning(0)
    else:
        for _ in range(len(ll2) - len(ll1)):
            ll1.add_to_beginning(0)

    n1, n2 = ll1.head, ll2.head
    result = 0
    while n1 and n2:
        result = (result * 10) + n1.value + n2.value
        n1 = n1.next
        n2 = n2.next

    return LinkedList([int(x) for x in str(result)])


def test_sum_lists(data):
    for ll1, ll2, expected in data:
        print(sum_lists(ll1, ll2))
        print(expected)


def test_follow_up(data):
    for ll1, ll2, expected in data:
        print(follow_up(ll1, ll2))
        print(expected)


if __name__ == "__main__":

    data = [(LinkedList([7, 1, 6]),
             LinkedList([5, 9, 2]),
             LinkedList([2, 1, 9]))]

    data2 = [(LinkedList([6, 1, 7]),
              LinkedList([2, 9, 5]),
              LinkedList([9, 1, 2]))]

    test_sum_lists(data)
    test_follow_up(data2)
