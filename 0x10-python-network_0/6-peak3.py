#!/usr/bin/python3
"""
6-peak.py

This module provides functions for getting the peak number in a integer list.

Functions:
- find_peak: Gets peak number

Usage example:
    import 6-peak
    result = 6-peak.find_peak([1,2,3,4])
"""


def find_peak(list_of_integers):
    """
    Finds the peak number.

    Parameters:
    - `list_of_integers` (list): List of integers.

    Returns:
    - int: Peak integer

    Example:
    ```python3
    result = find_peak([1,2,3])
    ```
    """
    if len(list_of_integers) == 0:
        return None
    peak = list_of_integers[0]
    for number in list_of_integers:
        if peak < number:
            peak = number
    return peak
