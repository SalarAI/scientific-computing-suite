import unittest
import numpy as np
from mathematics.vector_calculator import * 

class TestVectorCalculator(unittest.TestCase):
    def test_dot_product(self):
        A = [2, 4, 6]
        B = [1, 2, 3]
        C = 28
        res = DotProduct(A, B)
        np.testing.assert_almost_equal(res, C)

    def test_Cross_Product(self):
        A = [1, 0, 0]
        B = [0, 1, 0]
        C = [0, 0, 1]
        res = CrossProduct(A, B)
        np.testing.assert_almost_equal(res, C)

    def test_magnitude(self):
        x1, y1, z1 = 3, -2, 5
        x2, y2 = 3, 4
        CA = 6.164414003
        CB = 5
        resA = Magnitude(x1, y1, z1)
        resB = Magnitude(x2, y2)
        np.testing.assert_almost_equal(resA, CA)
        np.testing.assert_almost_equal(resB, CB)


    def test_projection(self):
        A = [3, 4]
        B = [4, 0]
        CS = 2.4
        CV = [1.44, 1.92]
        ress = Projection(A, B, type="scalar")
        resv = Projection(A, B, type="vector")
        np.testing.assert_almost_equal(ress, CS)
        np.testing.assert_almost_equal(resv, CV)


    def test_Angle_between_Vectors(self):
        A = [-2, 1]
        B = [3, 4]
        C = 1.750649826587375
        res = AngleBetweenVectors(A, B)
        np.testing.assert_almost_equal(res, C)

    def test_normalization(self):
        A = [1, 2, 3, 4]
        C = [0.18257419, 0.36514837, 0.54772256, 0.73029674]
        res = Normalization(A)
        np.testing.assert_almost_equal(res, C)
