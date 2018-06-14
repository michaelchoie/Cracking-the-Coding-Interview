# O(n)
import unittest


def unique(word):

    if len(word) >= 128:
        return False

    char_set = [False for _ in range(128)]

    for letter in word:
        val = ord(letter)
        if char_set[val]:
            return False
        char_set[ord(letter)] = True

    return True


class Test(unittest.TestCase):

    unique_dat = ["abcd", "ferty", ""]
    not_unique_dat = ["abab", "hb good morning"]

    def test_unique(self):
        for word in self.unique_dat:
            self.assertTrue(unique(word))

        for word in self.not_unique_dat:
            self.assertFalse(unique(word))


if __name__ == "__main__":
    unittest.main()
