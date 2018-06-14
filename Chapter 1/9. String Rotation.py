# O(n)
import unittest


def isSubstring(s1, s2):
    return s2 in s1


def string_rotation(s1, s2):
    if len(s1) == len(s2) != 0:
        return isSubstring(s1 + s1, s2)
    return False


class Test(unittest.TestCase):

    dataT = [("waterbottle", "erbottlewat")]

    dataF = [("hello", "goodbye")]

    def test_string_rotation(self):
        for strings in self.dataT:
            self.assertTrue(string_rotation(*strings))

        for strings in self.dataF:
            self.assertFalse(string_rotation(*strings))


if __name__ == "__main__":
    unittest.main()
