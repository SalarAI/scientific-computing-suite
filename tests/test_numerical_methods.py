import math
import unittest
from numerical_methods.Simpson_rule import *
from numerical_methods.secant import *
from numerical_methods.bisection import *
from numerical_methods.euler_method import *
from numerical_methods.runge_kutta import *
from numerical_methods.newton_method import *


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


class testnewtonmethods(unittest.TestCase):
    def test_newton_methods(self):
        f = lambda x: math.cos(x) - x**3
        f_prime = lambda x: -math.sin(x) - 3*x**2
        res = newton_raphson(f, f_prime, x0 = 0.5, max_iter = 6)
        C = 0.865474033102
        self.assertAlmostEqual(res, C)


class testsecantmethod(unittest.TestCase):
    def test_secant_method(self):
        f = lambda x: 2*x**3 - x - 3
        res = secant(f, x0 = 1, x1 = 2, n = 7)
        C = 1.289623901485061
        self.assertAlmostEqual(res, C)


class testrungekutta(unittest.TestCase):
    def test_rungge_kutta(self):
        f = lambda t, y : y
        res = runge_kutta(f, t0 = 0, y0 = 1, h = 0.1, n = 10)
        C = 2.718279744135166
        self.assertAlmostEqual(res, C)


class testbisection(unittest.TestCase):
    def test_bisection(self):
        f = lambda x: x**3 - x - 2
        res = bisection(1, 2, f, n = 15)
        C = 1.5213775634765625
        self.assertAlmostEqual(res, C)
