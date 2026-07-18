import unittest
from numerical_methods.Simpson_rule import *

class testSimpsonRule(unittest.TestCase):
    def test_simpson_rule_1_3(self):
        f = lambda x: x**2
        a, b = 0, 1
        C = 0.3333333333333333
        res = simpsonrule(a, b, f)
        self.assertAlmostEqual(res, C)
    
    def test_simpson_rule_3_8(self):
        f = lambda x: x**2
        a, b = 0, 1
        C = 0.3333333333333333
        res = simpsonrule(a, b, f, n=99 ,method="3/8")
        self.assertAlmostEqual(res, C)



