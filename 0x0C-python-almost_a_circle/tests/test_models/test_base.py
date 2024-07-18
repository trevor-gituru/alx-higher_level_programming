#!/usr/bin/python3
"""
#Trevor Muriuki <trevorx10x@gmail.com>

#####################
module: base.py
#####################
"""


import sys
import unittest
import inspect
import io
import pycodestyle
from contextlib import redirect_stdout
from models.base import Base


class TestSquare(unittest.TestCase):
    """tests Base class' methods"""
    def test_id(self):
        base1 = Base()
        base2 = Base()
        base3 = Base(89)
        self.assertNotEqual(base1.id, base2.id)
        self.assertEqual(base2.id, base1.id + 1)
        self.assertEqual(base3.id, 89)
    
    def test_to_json_string(self):
        json1 = Base.to_json_string(None)
        json2 = Base.to_json_string([])
        json3 = Base.to_json_string([ { 'id': 12 }])
        self.assertEqual(json1, '[]')
        self.assertEqual(json2, '[]')
        self.assertEqual(json3, '[{"id": 12}]')

    def test_from_json_string(self):
        string1 = Base.from_json_string(None)
        string2 = Base.from_json_string("[]")
        string3 = Base.from_json_string('[{ "id": 89 }]')
        self.assertEqual(string1, [])
        self.assertEqual(string2, [])
        self.assertEqual(string3, [{'id': 89}])
