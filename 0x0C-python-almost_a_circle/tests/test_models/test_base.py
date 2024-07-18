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
    def test_auto_id(self):
        base1 = Base()
        base2 = Base()
        self.assertNotEqual(base1.id, base2)

    def test_auto_id_prev(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base2.id, base1.id + 1)
