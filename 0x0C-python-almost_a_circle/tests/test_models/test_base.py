#!/usr/bin/python3
"""Unittest module for class Base"""
import unittest
from models.base import Base
from models.rectangle import Rectangle



class TestBase(unittest.TestCase):
    """Test cases for the base class"""
    def test_instance(self):
        """test instantiation"""
        self.assertIsInstance(Base(), Base)
    
    def test_id(self):
        """test for instance id"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, b2.id * 2)
    
    def test_edge_id(self):
        """test for negative id"""
        b5 = Base(0)
        self.assertEqual(b5.id, 0)
        b5 = Base(-16)
        self.assertEqual(b5.id, -16)
    
    def test_string_id(self):
        """test for string id"""
        new = Base('1')
        self.assertEqual(new.id, '1')
    
    def test_private_id(self):
        """trying to access private attr id"""
        b1 = Base(15)
        with self.assertRaises(AttributeError):
            print(b1.__nb_instances)

    #def test_


if __name__ == "__main__":
    unittest.main()
