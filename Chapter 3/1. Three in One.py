# Use one array to implement three stacks
from Stack import Stack
import unittest


class Test(unittest.TestCase):

    def test(self):
        data = Stack(stack_size=2, num_stacks=3)
        data.push(5, 0)
        data.push(8, 0)
        data.push(5, 1)

        self.assertTrue(data.is_full(0))
        self.assertEqual(data.pop(0), 8)
        self.assertTrue(data.is_empty(2))
        self.assertEqual(data.index_of_top(1), 2)


if __name__ == "__main__":
    unittest.main()
