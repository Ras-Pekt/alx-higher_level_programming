#!/usr/bin/python3
"""unit tests for the Rectangle class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_normal_case(self):
        r = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.id, 1)

    def test_width_type_error(self):
        with self.assertRaises(TypeError):
            r = Rectangle("invalid", 10, 2, 3, 1)

    def test_height_type_error(self):
        with self.assertRaises(TypeError):
            r = Rectangle(5, "invalid", 2, 3, 1)

    def test_x_type_error(self):
        with self.assertRaises(TypeError):
            r = Rectangle(5, 10, "invalid", 3, 1)

    def test_y_type_error(self):
        with self.assertRaises(TypeError):
            r = Rectangle(5, 10, 2, "invalid", 1)

    def test_width_value_error(self):
        with self.assertRaises(ValueError):
            r = Rectangle(0, 10, 2, 3, 1)

    def test_height_value_error(self):
        with self.assertRaises(ValueError):
            r = Rectangle(5, 0, 2, 3, 1)

    def test_x_value_error(self):
        with self.assertRaises(ValueError):
            r = Rectangle(5, 10, -2, 3, 1)

    def test_y_value_error(self):
        with self.assertRaises(ValueError):
            r = Rectangle(5, 10, 2, -3, 1)

    def test_area(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

    def test_update_args(self):
        r = Rectangle(5, 10, 2, 3, 1)
        r.update(7, 15, 1, 2, 4)
        self.assertEqual(r.width, 15)
        self.assertEqual(r.height, 1)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.id, 7)

    def test_update_kwargs(self):
        r = Rectangle(5, 10, 2, 3, 1)
        r.update(width=7, height=15, x=1, y=2, id=4)
        self.assertEqual(r.width, 7)
        self.assertEqual(r.height, 15)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.id, 4)

    def test_to_dictionary(self):
        r = Rectangle(5, 10, 2, 3, 1)
        expected_dict = {'x': 2, 'y': 3, 'id': 1, 'height': 10, 'width': 5}
        self.assertEqual(r.to_dictionary(), expected_dict)    

    def test_set_width_type_error(self):
        with self.assertRaises(TypeError):
            Rectangle("invalid", 10)

    def test_set_width_value_error(self):
        with self.assertRaises(ValueError):
            Rectangle(-5, 10)

    def test_set_height_type_error(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "invalid")

    def test_set_height_value_error(self):
        with self.assertRaises(ValueError):
            Rectangle(10, -5)

    def test_set_x_type_error(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 10, "invalid")

    def test_set_x_value_error(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 10, -5)

    def test_set_y_type_error(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 10, 5, "invalid")

    def test_set_y_value_error(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 10, 5, -5)
