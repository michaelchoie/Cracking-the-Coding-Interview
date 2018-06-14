# O(n)
import unittest


def one_away(str1, str2):

    if len(str1) == len(str2):
        return one_away_same(str1, str2)
    elif len(str1) + 1 == len(str2):
        return one_away_insert(str1, str2)
    elif len(str1) - 1 == len(str2):
        return one_away_insert(str2, str1)

    return False


def one_away_same(str1, str2):

    edits = False

    for letter1, letter2 in zip(str1, str2):
        if letter1 != letter2:
            if edits:
                return False
            edits = True

    return True


def one_away_insert(str1, str2):

    edits = False
    x, y = 0, 0

    while x < len(str1) and y < len(str2):
        if str1[x] != str2[y]:
            if edits:
                return False
            edits = True
            y += 1
        else:
            x += 1
            y += 1

    return True


class Test(unittest.TestCase):

    dataT = [("hello", "hell"),
             ("hello", "jello"),
             ("", "h")]
    dataF = [("hi", "hello"),
             ("", "hi")]

    def test_one_away(self):

        for words in self.dataT:
            self.assertTrue(one_away(*words))

        for words in self.dataF:
            self.assertFalse(one_away(*words))


if __name__ == "__main__":
    unittest.main()
