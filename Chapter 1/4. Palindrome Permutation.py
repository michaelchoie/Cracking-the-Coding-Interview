# O(n)
from collections import Counter
import unittest

def palindrome_permutation(phrase):

    counter = Counter(phrase)
    count = 0
    for entry in counter:
        count += counter[entry] % 2
    return count <= 1


class Test(unittest.TestCase):

    def test_palindrome_permutation(self, phrase):
        dataT = ["poop", "racecar", "tact coa"]
        dataF = ["hello", "mr. poopybutthole"]

        for word in self.dataT:
            self.assertTrue(palindrome_permutation(word))

        for word in self.dataF:
            self.assertFalse(palindrome_permutation(word))

if __name__ == "__main__":
    unittest.main()
