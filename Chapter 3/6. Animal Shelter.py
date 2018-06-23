"""Create a data structure to maintain the animal shelter system"""


class Node(object):

    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next = next_node
        self.prev = prev_node

    def __str__(self):
        return str(self.value)


class Animal(Node):

    def __init__(self, species, value, next_node=None, prev_node=None):
        super().__init__(value, next_node, prev_node)
        self.species = species

    def __str__(self):
        return 'Species: %s, Priority: %d ' % (self.species, self.value)


class LinkedList(object):

    def __init__(self, values=None):
        self.head = None
        self.tail = None
        if values:
            self.add_multiple(values)

    def __iter__(self):
        current = self.head

        while current:
            yield current
            current = current.next

    def __len__(self):
        counter = 0
        current = self.head

        while current:
            current = current.next
            counter += 1

        return counter

    def __str__(self):
        values = [str(x) for x in self]
        return ' '.join(values)

    def add(self, value):
        if not isinstance(value, Node):
            value = Node(value)

        if self.head is None:
            self.head = value
            self.tail = value
        else:
            self.tail.next = value
            self.tail = self.tail.next

        return self.tail

    def add_multiple(self, values):
        for value in values:
            self.add(value)

    def add_to_beginning(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = Node(value)
        else:
            self.head = Node(value, nextNode=self.head)

        return self.head

    def remove_from_beginning(self):
        if self.head is None:
            raise Exception("Empty list")

        node = self.head
        if self.head and self.head.next:
            self.head = self.head.next
            self.head.prev = None
        else:
            self.head = self.tail = None

        return node


class AnimalShelter(object):

    def __init__(self):
        self.cats = LinkedList()
        self.dogs = LinkedList()
        self.order = 0

    def enqueue(self, animal):
        self.order += 1
        node = Animal(animal, self.order)

        if animal == "cat":
            self.cats.add(node)
        else:
            self.dogs.add(node)

    def dequeue_any(self):
        if len(self.cats) == 0 and len(self.dogs) == 0:
            raise Exception("Empty Shelter")

        if self.cats.head.value > self.dogs.head.value:
            value = self.dequeue_dog()
        elif self.dogs.head.value > self.cats.head.value:
            value = self.dequeue_cat()

        return value

    def dequeue_dog(self):
        return self.dogs.remove_from_beginning()

    def dequeue_cat(self):
        return self.cats.remove_from_beginning()


def test_animal_shelter():
    shelter = AnimalShelter()
    shelter.enqueue('cat')
    shelter.enqueue('dog')
    shelter.enqueue('cat')

    print(shelter.dequeue_any())
    print(shelter.dequeue_dog())
    print(shelter.dequeue_cat())


if __name__ == "__main__":
    test_animal_shelter()
