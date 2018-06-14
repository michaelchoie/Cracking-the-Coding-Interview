# O(m*n)
import numpy as np
import unittest


def zero_matrix(matrix):

    nrow, ncol = matrix.shape
    coordinates = []

    for row in range(nrow):
        for col in range(ncol):
            if matrix[row, col] == 0:
                coordinates.append((row, col))

    for row, col in coordinates:
        matrix[row, :] = 0
        matrix[:, col] = 0

    return matrix


class Test(unittest.TestCase):

    data = [(np.array([[1, 2, 3],
                       [0, 4, 5],
                       [0, 6, 7]]),
             np.array([[0, 2, 3],
                       [0, 0, 0],
                       [0, 0, 0]]))]

    def test_zero_matrix(self):
        for input_array, expected in self.data:
            np.testing.assert_array_equal(zero_matrix(input_array), expected)


if __name__ == "__main__":
    unittest.main()
