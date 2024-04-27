import unittest
from models.base import Base
from models.square import Square
import sys
from io import StringIO

class TestSquare(unittest.TestCase):

    def setUp(self):
        # Reset the counter before each test
        Base._Base__nb_objects = 0
        self.s = Square(2)

    def test_initialization(self):
        self.assertEqual(self.s.size, 2)
        self.assertEqual(self.s.x, 0)
        self.assertEqual(self.s.y, 0)
        self.assertEqual(self.s.id, 1)

    def test_area(self):
        self.assertEqual(self.s.area(), 4)

    def test_display(self):
        self.s.x = 2
        self.s.y = 2

        # Redirect stdout to capture printed output
        captured_output = StringIO()
        sys.stdout = captured_output

        self.s.display()

        # Restore stdout
        sys.stdout = sys.__stdout__

        expected_output = '\n\n  ##\n  ##\n'
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_to_string(self):
        s = Square(2, 2, 2, 10)
        self.assertEqual(str(s), "[Square] (10) 2/2 - 2")

    def test_update_method(self):
        self.s.update(10, 5, 5, 5)
        self.assertEqual(self.s.size, 5)
        self.assertEqual(self.s.x, 5)
        self.assertEqual(self.s.y, 5)


    def test_setters(self):
        self.s.size = 10
        self.assertEqual(self.s.size, 10)
        with self.assertRaises(TypeError):
            self.s.size = "invalid"
        with self.assertRaises(ValueError):
            self.s.size = -10

        # Repeat similar tests for x and y setters

        self.s.x = 5
        self.assertEqual(self.s.x, 5)
        with self.assertRaises(ValueError):
            self.s.x = -5

        self.s.y = 5
        self.assertEqual(self.s.y, 5)
        with self.assertRaises(ValueError):
            self.s.y = -5


if __name__ == '__main__':
    unittest.main()
