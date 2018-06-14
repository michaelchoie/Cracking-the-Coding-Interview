# O(n^2)
import numpy as np
import unittest


def rotate_matrix(matrix):
    '''Clockwise rotation 90 degrees'''
    nrow, ncol = matrix.shape

    top = np.copy(matrix[0, :])
    # left side --> top
    matrix[0, :] = matrix[:, 0][::-1]
    # bottom --> left side
    matrix[:, 0] = matrix[nrow - 1, :]
    # right side --> bottom
    matrix[nrow - 1, :] = matrix[:, ncol - 1][::-1]
    # top --> right side
    matrix[:, ncol - 1] = top

    return matrix


class Test(unittest.TestCase):

    data = [(np.array([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]]),
             np.array([[7, 4, 1],
                       [8, 5, 2],
                       [9, 6, 3]]))]

    def test_rotate_matrix(self):
        for matrix, expected in self.data:
            np.testing.assert_array_equal(rotate_matrix(matrix), expected)


if __name__ == "__main__":
    unittest.main()
