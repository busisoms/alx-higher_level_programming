import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os

class TestBase(unittest.TestCase):

    def setUp(self):
        # Create a test directory to store JSON files
        self.test_dir = 'test_files'
        os.makedirs(self.test_dir, exist_ok=True)

    def tearDown(self):
        # Remove the test directory and its contents
        os.rmdir(self.test_dir)

    def test_base_constructor(self):
        # Create instances of Base without specifying ID
        base1 = Base()
        base2 = Base()

        # Check if IDs are assigned correctly
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)

        # Create instances of Base with specified ID
        base3 = Base(10)
        base4 = Base(20)

        # Check if IDs are assigned correctly
        self.assertEqual(base3.id, 10)
        self.assertEqual(base4.id, 20)

    def test_to_json_string(self):
        # Test to_json_string method with empty list
        self.assertEqual(Base.to_json_string([]), "[]")

        # Test to_json_string method with list of dictionaries
        dicts = [{'id': 1, 'width': 10, 'height': 5}, {'id': 2, 'width': 7, 'height': 3}]
        self.assertEqual(Base.to_json_string(dicts), '[{"id": 1, "width": 10, "height": 5}, {"id": 2, "width": 7, "height": 3}]')

    def test_from_json_string(self):
        # Test from_json_string method with empty string
        self.assertEqual(Base.from_json_string(''), [])

        # Test from_json_string method with valid JSON string
        json_str = '[{"id": 1, "width": 10, "height": 5}, {"id": 2, "width": 7, "height": 3}]'
        self.assertEqual(Base.from_json_string(json_str), [{'id': 1, 'width': 10, 'height': 5}, {'id': 2, 'width': 7, 'height': 3}])

    def test_save_and_load_from_file(self):
        # Create some Rectangle instances
        r1 = Rectangle(10, 5)
        r2 = Rectangle(7, 3)

        # Save instances to file
        Rectangle.save_to_file([r1, r2])

        # Load instances from file
        loaded_rectangles = Rectangle.load_from_file()

        # Check if loaded rectangles match original ones
        self.assertEqual(len(loaded_rectangles), 2)
        self.assertEqual(loaded_rectangles[0].to_dictionary(), r1.to_dictionary())
        self.assertEqual(loaded_rectangles[1].to_dictionary(), r2.to_dictionary())

    def test_save_and_load_from_file_for_square(self):
        # Create some Square instances
        s1 = Square(5)
        s2 = Square(3)

        # Save instances to file
        Square.save_to_file([s1, s2])

        # Load instances from file
        loaded_squares = Square.load_from_file()

        # Check if loaded squares match original ones
        self.assertEqual(len(loaded_squares), 2)
        self.assertEqual(loaded_squares[0].to_dictionary(), s1.to_dictionary())
        self.assertEqual(loaded_squares[1].to_dictionary(), s2.to_dictionary())

    def test_create(self):
        # Test create method for Rectangle
        rect_dict = {'id': 1, 'width': 10, 'height': 5, 'x': 2, 'y': 3}
        rect = Rectangle.create(**rect_dict)
        self.assertEqual(rect.to_dictionary(), rect_dict)

        # Test create method for Square
        square_dict = {'id': 2, 'size': 5, 'x': 1, 'y': 1}
        square = Square.create(**square_dict)
        self.assertEqual(square.to_dictionary(), square_dict)

if __name__ == '__main__':
    unittest.main()
