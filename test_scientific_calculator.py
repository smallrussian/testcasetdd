from unittest import TestCase, main as unittestmain
from scientific_calculator import sin, cos, tan, sqrt, log, exp

class MyCalculatorTest(TestCase):
    
    def test_sin(self):
        self.assertEqual(sin(0), 0)
        self.assertEqual(sin(1), 0.8414709848078965)
        self.assertEqual(sin(-1), -0.8414709848078965)
        self.assertRaises(TypeError, "exp")
        
    def test_cos(self):
        self.assertEqual(cos(0), 1)
        self.assertEqual(cos(1), 0.5403023058681398)
        self.assertEqual(cos(-1), 0.5403023058681398)
        self.assertRaises(TypeError, "exp")
        
    def test_tan(self):
        self.assertEqual(tan(0), 0)
        self.assertEqual(tan(1), 1.5574077246549023)
        self.assertEqual(tan(-1), -1.5574077246549023)
        self.assertRaises(TypeError, "exp")
        
    def test_sqrt(self):
        self.assertEqual(sqrt(0), 0)
        self.assertEqual(sqrt(1), 1)
        self.assertEqual(sqrt(4), 2)
        self.assertRaises(TypeError, log, "exp")
        self.assertRaises(ValueError, sqrt, -1)
        
    def test_log(self):
        self.assertEqual(log(1), 0)
        self.assertEqual(log(10), 2.302585092994046)
        self.assertEqual(log(100), 4.605170185988092)
        self.assertRaises(TypeError,log, "exp")
        self.assertRaises(ValueError, log, -1)
        
    def test_exp(self):
        self.assertEqual(exp(0), 1)
        self.assertEqual(exp(2), 7.38905609893065)
        self.assertEqual(exp(3), 20.085536923187668)
        self.assertRaises(TypeError, exp, "exp")
        
        
    
        
        
if __name__ == '__main__':
    unittestmain()