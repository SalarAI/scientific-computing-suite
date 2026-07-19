import unittest
from numerical_methods.trapezoidal_rule import *

class TestTrapezoidalRule(unittest.TestCase):
    def testtrapezoidalrule(self):
        a, b = 1, 3
        f = lambda x: 1 / x
        c = 1.1301587301587301
        res = trapezoidal_rule(a, b, f, n=3)
        self.assertAlmostEqual(res, c)
        
        
