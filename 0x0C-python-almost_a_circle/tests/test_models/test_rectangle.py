import unittest
from models.base import Base
from models.rectangle import Rectangle
import sys
from io import StringIO

class TestRectangle(unittest.TestCase):

    def setUp(self):
        # Reset the counter before each test
        Base._Base__nb_objects = 0
        self.r = Rectangle(2, 3)

    def test_initialization(self):
        self.assertEqual(self.r.width, 2)
        self.assertEqual(self.r.height, 3)
        self.assertEqual(self.r.x, 0)
        self.assertEqual(self.r.y, 0)
        self.assertEqual(self.r.id, 1)

    def test_area(self):
        self.assertEqual(self.r.area(), 6)

    def test_display(self):
        self.r.x = 2
        self.r.y = 2

        # Redirect stdout to capture printed output
        captured_output = StringIO()
        sys.stdout = captured_output

        self.r.display()

        # Restore stdout
        sys.stdout = sys.__stdout__

        expected_output = '\n\n  ##\n  ##\n  ##\n'
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_to_string(self):
        r = Rectangle(2, 3, 2, 2)
        self.assertEqual(str(r), "[Rectangle] (2) 2/2 - 2/3")

    def test_update_method(self):
        self.r.update(10, 5, 5, 5, 5)
        self.assertEqual(self.r.width, 5)
        self.assertEqual(self.r.height, 5)
        self.assertEqual(self.r.x, 5)
        self.assertEqual(self.r.y, 5)

    def test_setters(self):
        self.r.width = 10
        self.assertEqual(self.r.width, 10)
        with self.assertRaises(TypeError):
            self.r.width = "invalid"
        with self.assertRaises(ValueError):
            self.r.width = -10

        # Repeat similar tests for height, x, and y setters

        self.r.x = 5
        self.assertEqual(self.r.x, 5)
        with self.assertRaises(ValueError):
            self.r.x = -5

        self.r.y = 5
        self.assertEqual(self.r.y, 5)
        with self.assertRaises(ValueError):
            self.r.y = -5

    def test_to_dictionary(self):
        expected_dict = {'id': 1, 'width': 2, 'height': 3, 'x': 0, 'y': 0}
        self.assertEqual(self.r.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
