from LinkedList import LinkedList


def delete_middle_node(node):

    node.value = node.next.value
    node.next = node.next.next


def test():

    data = LinkedList(['a', 'b'])
    middle_node = data.add('c')
    data.add_multiple(['d', 'e', 'f'])

    print(data)
    delete_middle_node(middle_node)
    print(data)


if __name__ == "__main__":
    test()
