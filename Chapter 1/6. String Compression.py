# O(n)
import unittest


def string_compression(word):

    compressed_string = []
    count = 0

    for x in range(len(word)):
        if x != 0 and word[x] != word[x - 1]:
            compressed_string.append("%s%d" % (word[x - 1], count))
            count = 0
        count += 1

    compressed_string.append("%s%d" % (word[-1], count))

    if len(compressed_string) >= len(word):
        return word
    else:
        return compressed_string


class Test(unittest.TestCase):

    data = [("aabcccccaaa", "a2b1c5a3"),
            ("abcd", "abcd")]

    def test_string_compression(self):

        for word, expected in self.data:
            self.assertEqual(''.join(string_compression(word)), expected)


if __name__ == "__main__":
    unittest.main()
