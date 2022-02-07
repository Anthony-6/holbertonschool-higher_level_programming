#!/usr/bin/python3
"""
Add unit test for the class Base
"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseInstance(unittest.TestCase):
    """
    This class test the class Base about the instance.
    """

    def tests_instance(self):
        """
        Tests about:
            - positive integers
            - negative integers
            - boolean
            - string
            - tuple
            - set
            - list
            - empty
            - None
        """
        b = Base(1)
        self.assertEqual(b.id, 1)
        b = Base(12)
        self.assertEqual(b.id, 12)
        b = Base(201)
        self.assertEqual(b.id, 201)

        b = Base(-1)
        self.assertEqual(b.id, -1)
        b = Base(-12)
        self.assertEqual(b.id, -12)

        b = Base(True)
        self.assertEqual(b.id, True)

        b = Base('hello')
        self.assertEqual(b.id, 'hello')

        b = Base((1, 2, 3))
        self.assertEqual(b.id, (1, 2, 3))
        b = Base({1, 2, 3})
        self.assertEqual(b.id, {1, 2, 3})
        b = Base([1, 2, 3])
        self.assertEqual(b.id, [1, 2, 3])
        b = Base({'name': 'holberton', 'age': 6})
        self.assertEqual(b.id, {'name': 'holberton', 'age': 6})

        b = Base()
        self.assertEqual(b.id, 1)
        b = Base(None)
        self.assertEqual(b.id, 2)

    def tests_instance_error(self):
        """
        TESTS EXCEPTIONS:
            - more than one argument
        A test about the message is implemented.
        """
        with self.assertRaises(TypeError) as m:
            Base(1, 1)
        error_message = '__init__() takes from 1 to 2 positional arguments' \
                        ' but 3 were given'
        self.assertEqual(error_message, str(m.exception))


class TestBaseToJsonString(unittest.TestCase):
    """
    This class test the class Base about the function 'to_json_string()'.
    """

    def tests_to_json_string_error(self):
        """
         TESTS EXCEPTIONS:
             - without argument
             - with too much argument
         """
        with self.assertRaises(TypeError):
            Base.to_json_string()

        with self.assertRaises(TypeError):
            Base.to_json_string([{1, 2, 3}], [{4, 5, 6}])


class TestBaseSaveToFile(unittest.TestCase):
    """
    This class test the class Base about the function 'save_to_file()'.
    """

    def tests_save_to_file_error(self):
        """
        TESTS EXCEPTIONS:
            - if list_objs is None for Rectangle file
            - if list_objs is None for Square file
        """
        Rectangle.save_to_file(None)
        list_objs = '"[]"'
        with open('Rectangle.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(), list_objs)
        os.remove('Rectangle.json')

        Square.save_to_file(None)
        list_objs = '"[]"'
        with open('Square.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(), list_objs)
        os.remove('Square.json')
