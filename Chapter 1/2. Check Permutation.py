# O(n)
import unittest
from collections import Counter


def check_permutation(str1, str2):

    if len(str1) != len(str2):
        return False

    counter = Counter(str1)
    for letter in str2:
        if counter[letter] == 0:
            return False
        counter[letter] -= 1

    return True


class Test(unittest.TestCase):

    dataT = [("abcd", "dbac"),
             ("1324", "1234")]
    dataF = [("abcd", "efgh"),
             ("abcd", "efg")]

    def test_check_permutation(self):
        for strings in self.dataT:
            self.assertTrue(check_permutation(*strings))

        for strings in self.dataF:
            self.assertFalse(check_permutation(*strings))


if __name__ == "__main__":
    unittest.main()