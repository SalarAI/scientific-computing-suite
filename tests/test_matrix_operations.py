import unittest
import numpy as np
from mathematics import *

class TestMath(unittest.TestCase):
    def test_add(self):
        A = [[1, 3, 1], [1, 0, 0]]
        B = [[0, 0, 5], [7, 5, 0]]
        C = np.array([[1., 3., 0.], [8., 5., 0.]])
        result = matrix_add(A, B)
        np.testing.assert_array_equal(result, C)
    
    def test_sub(self):
        A = [[1, 3, 1], [1, 0, 0]]
        B = [[0, 0, 5], [7, 5, 0]]
        C = np.array([[1, 3, 0], [-6, -5, 0]])
        result = matrix_sub(A, B)
        np.testing.assert_array_almost_equal(result, C)
    
    def test_multiplication(self):
        A = [[1, 8, 3], [9, 4, 5], [6, 2, 7]]
        B = [[6, 7, 4], [1, 3, 2], [5, 9, 8]]
        C = np.array([[29., 58., 44], [83., 120., 84], [73., 111., 84]])
        result = matrix_multiplication(A, B)
        np.testing.assert_almost_equal(result, C)

    def test_transpose(self):
        A = [[1, 3, 5], [2, 4, 6]]
        C = np.array([[1, 2], [3, 4], [5, 6]])
        result = transpose(A)
        np.testing.assert_almost_equal(result, C)

    def test_inverse(self):
        A = [[4, 3], [3, 2]]
        C = np.array([[-2, 3], [3, -4]])
        result = inverse(A)
        np.testing.assert_almost_equal(result, C)

    def test_rank(self):
        A = [[1, 2, 3], [2, 4, 6], [1, 1, 1]]
        C = 2
        result = rank(A)
        np.testing.assert_almost_equal(result, C)

    def test_determinate(self):
        A = [[3, 7], [1, -4]]
        C = -19
        result = determinat(A)
        np.testing.assert_almost_equal(result, C)

    def test_gaussian_elimination(self):
        A = [[4, 3], [6, 3]]
        b = [10, 12]
        C = np.array([1., 2.])
        result = gaussian_elimination(A, b)
        np.testing.assert_almost_equal(result, C)

    def test_LU(self):
        A = [[4, 3], [6, 3]]
        L_result = np.array([[1, 0], [1.5, 1]])
        U_result = np.array([[4, 3], [0, -1]])
        L, U = LU(A)
        np.testing.assert_almost_equal(L ,L_result)
        np.testing.assert_almost_equal(U ,U_result)
