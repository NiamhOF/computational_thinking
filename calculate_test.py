import unittest
from calculate import calculate

class TestCalculate (unittest.TestCase):
    def testCalculation (self):
        self.assertEqual (calculate (3,3), 6)
        self.assertEqual (calculate (3,4), 7)
        self.assertEqual (calculate (5,5), 10)

if __name__ == '__main__':
    unittest.main()
