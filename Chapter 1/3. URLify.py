# O(n)
import unittest


def URLify(word, length):

    word_length = len(word)
    if length == word_length:
        return word

    for x in reversed(range(length)):
        if word[x] == " ":
            word[word_length - 3:word_length] = "%20"
            word_length -= 3
        else:
            word[word_length - 1] = word[x]
            word_length -= 1

    return word


class Test(unittest.TestCase):

    dataT = [(list("he llo  "), 6, list("he%20llo")),
             (list("he l lo    "), 7, list("he%20l%20lo"))]

    def test_URLify(self):
        for word, length, expected in self.dataT:
            actual = URLify(word, length)
            self.assertTrue(actual, expected)


if __name__ == "__main__":
    unittest.main()
