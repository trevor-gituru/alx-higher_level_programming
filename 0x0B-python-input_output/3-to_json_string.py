#!/usr/bin/python3
"""
3-to_json_string.py

This module contains only to_json_ string(obj) function.

Functions:
- to_json_ string(obj)": Returns a json form of obj
"""

import json


def to_json_string(my_obj):
    """
    Returns a json form of obj

    Args:
        my_obj: The object to be converted.

    Returns:
         Returns a json form of obj
    """
    return json.dumps(my_obj)
