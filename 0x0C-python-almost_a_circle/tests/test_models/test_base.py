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
        self.assertEqual(base1.id, 1)
