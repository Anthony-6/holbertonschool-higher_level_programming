#!/usr/bin/python3
"""
Add unit test for the class Square.
test if attributes are correct
test if square inherit correctly or not
test if argument are the good type raise error if not
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class testSquare(unittest.TestCase):

    def testSquareHeight(self):
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.height, 1)

    def testSquareWidth(self):
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.width, 1)

    def testSquareX(self):
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.x, 2)

    def testSquareY(self):
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.y, 3)

    def testSquareId(self):
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.id, 4)

    def testRectInherint(self):
        s = Square(5)
        self.assertTrue(isinstance(s, Rectangle))

    def testBaseInherint(self):
        s = Square(5)
        self.assertTrue(isinstance(s, Base))

    def testBaseSubClass(self):
        s = Square(5)
        self.assertTrue(issubclass(Square, Base))

    def testRectSubClass(self):
        s = Square(5)
        self.assertTrue(issubclass(Square, Rectangle))

    def testSrBaseInherint(self):
        self.assertFalse(isinstance(Square, Base))

    def testSrRectInherit(self):
        self.assertFalse(isinstance(Square, Rectangle))

    def testSquareArea(self):
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def testUpdate(self):
        s1 = Square(1, 1, 1, 1)
        s1.update(1, 1, 1, 5)
        self.assertEqual(s1.id, 1)

    def testSize(self):
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.size, 1)

    def testErrorWidth(self):
        with self.assertRaises(TypeError):
            s = Square('Square', 1)
            s.width()

    def testErrorX(self):
        with self.assertRaises(TypeError):
            s = Square(1, 'not a square')
            s.x()

    def testErrorY(self):
        with self.assertRaises(TypeError):
            s = Square(1, 2, 'hehe')
            s.y()

    def testErrorId(self):
        with self.assertRaises(TypeError):
            s = Square(1, 3, 4, 'five')
            s.id()

    def testZeroWidth(self):
        with self.assertRaises(ValueError):
            s = Square(0)
            s.width()

    def testNegativWidth(self):
        with self.assertRaises(ValueError):
            s = Square(-1)
            s.width()

    def testNegativX(self):
        with self.assertRaises(ValueError):
            s = Square(1, -5)
            s.x()

    def testNegativY(self):
        with self.assertRaises(ValueError):
            s = Square(1, 2, -3, 5)
            s.y()

    def testNegativId(self):
        with self.assertRaises(TypeError):
            s = Square(1, 2, 3, -5)
            s.id()


if __name__ == "__main__":
    unittest.main()
