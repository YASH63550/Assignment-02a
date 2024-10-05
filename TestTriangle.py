import unittest
from Triangle import classifyTriangle

class TestTriangles(unittest.TestCase):
    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testIsoscelesTriangle(self):
        self.assertEqual(classifyTriangle(2,2,3),'Isosceles','2,2,3 should be isosceles')

    def testScaleneTriangle(self):
        self.assertEqual(classifyTriangle(3,4,6),'Scalene','3,4,6 should be scalene')

    def testInvalidInput(self):
        self.assertEqual(classifyTriangle(201,3,4),'InvalidInput','201,3,4 should be invalid input')
        self.assertEqual(classifyTriangle(-1,2,3),'InvalidInput','-1,2,3 should be invalid input')
        self.assertEqual(classifyTriangle(1.5,2,3),'InvalidInput','1.5,2,3 should be invalid input')

    def testNotATriangle(self):
        self.assertEqual(classifyTriangle(1,1,3),'NotATriangle','1,1,3 is not a triangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()