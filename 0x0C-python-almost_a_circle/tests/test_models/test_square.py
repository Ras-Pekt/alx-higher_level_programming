#!/usr/bin/python3
"""unit tests for the Square class"""
import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_constructor(self):
        """Test constructor with default values"""
        square = Square(5)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)

    def test_custom_constructor(self):
        """Test constructor with custom values"""
        square = Square(10, 2, 3, 1)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.width, 10)
        self.assertEqual(square.height, 10)

    def test_str(self):
        """test str function"""
        square = Square(5, 1, 2, 3)
        self.assertEqual(str(square), "[Square] (3) 1/2 - 5")

    def test_size_property(self):
        square = Square(5)
        square.size = 10
        self.assertEqual(square.size, 10)
        self.assertEqual(square.width, 10)
        self.assertEqual(square.height, 10)

    def test_update_args(self):
        """test update function on args"""
        square = Square(5)
        square.update(1, 10, 2, 3)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.width, 10)
        self.assertEqual(square.height, 10)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_update_kwargs(self):
        """test update function on kwargs"""
        square = Square(5)
        square.update(id=5, x=7, y=8)
        self.assertEqual(square.id, 5)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 7)
        self.assertEqual(square.y, 8)

    def test_init_invalid_width(self):
        """Test initialization with invalid width"""
        with self.assertRaises(ValueError):
            Square(0, 2, 3, 10)

    def test_init_invalid_height(self):
        """Test initialization with invalid height"""
        with self.assertRaises(ValueError):
            Square(-5, 2, 3, 10)

    def test_init_invalid_x(self):
        """Test initialization with invalid x"""
        with self.assertRaises(ValueError):
            Square(5, -2, 3, 10)

    def test_init_invalid_y(self):
        """Test initialization with invalid y"""
        with self.assertRaises(ValueError):
            Square(5, 2, -3, 10)

    def test_size_setter_invalid(self):
        """Test setter with invalid size"""
        with self.assertRaises(ValueError):
            Square(-5)

    def test_size_setter_type_error(self):
        """Test setter with invalid type for size"""
        with self.assertRaises(TypeError):
            Square('invalid')

    def test_x_setter_invalid(self):
        """Test setter with invalid x"""
        with self.assertRaises(ValueError):
            Square(-2)

    def test_x_setter_type_error(self):
        """Test setter with invalid type for x"""
        with self.assertRaises(TypeError):
            Square('invalid')

    def test_y_setter_invalid(self):
        """Test setter with invalid y"""
        with self.assertRaises(ValueError):
            Square(-3)

    def test_y_setter_type_error(self):
        """Test setter with invalid type for y"""
        with self.assertRaises(TypeError):
            Square('invalid')


if __name__ == "__main__":
    unittest.main()
