#!/usr/bin/python3
"""
13-pascal_triangle
"""


def pascal_triangle(n):
    """Creates the pascal triangle

    Args:
        n : Size of pascal triangle
    Return:
        The pascal triangle as a list of list of integers
    """
    pascal_list = []
    if n <= 0:
        return pascal_list
    pascal_list.append([1])
    if n == 1:
        return pascal_list
    pascal_list.append([1, 1])
    if n == 2:
        return pascal_list
    # N = 3 [[1], [1,1]]
    for triangle in range(1, n - 1):
        # Add first element
        triangle_list = [1]
        # Get previous triangle list
        prev_triangle = pascal_list[triangle]
        for element in range(len(prev_triangle) - 1):
            consec_sum = prev_triangle[element] + prev_triangle[element + 1]
            triangle_list.append(consec_sum)
        # Add last element
        triangle_list.append(1)
        pascal_list.append(triangle_list)
    return pascal_list
